"""
Automated tests for VehicleService.
"""

import pytest

from app.models.car import Car
from app.models.motorcycle import Motorcycle
from app.models.truck import Truck
from app.services.vehicle_service import VehicleService


def create_car():
    """Create a test car."""

    return Car(
        "CAR-001",
        "Toyota",
        "Corolla",
        2023,
        4,
        "petrol"
    )


def create_motorcycle():
    """Create a test motorcycle."""

    return Motorcycle(
        "MOTO-001",
        "Yamaha",
        "R1",
        2024,
        2,
        "sport"
    )


def create_truck():
    """Create a test truck."""

    return Truck(
        "TRK-001",
        "Volvo",
        "FH16",
        2022,
        25,
        "automatic"
    )


def test_service_starts_empty():
    """Test that the service starts with no vehicles."""

    service = VehicleService()

    assert service.get_vehicle_count() == 0
    assert service.get_all_vehicles() == []


def test_add_vehicle():
    """Test adding a vehicle."""

    service = VehicleService()
    car = create_car()

    service.add_vehicle(car)

    assert service.get_vehicle_count() == 1
    assert service.find_vehicle_by_id("CAR-001") is car


def test_add_multiple_vehicle_types():
    """Test polymorphic vehicle management."""

    service = VehicleService()

    car = create_car()
    motorcycle = create_motorcycle()
    truck = create_truck()

    service.add_vehicle(car)
    service.add_vehicle(motorcycle)
    service.add_vehicle(truck)

    assert service.get_vehicle_count() == 3

    vehicles = service.get_all_vehicles()

    assert car in vehicles
    assert motorcycle in vehicles
    assert truck in vehicles


def test_invalid_vehicle_rejected():
    """Test that invalid objects are rejected."""

    service = VehicleService()

    with pytest.raises(TypeError):
        service.add_vehicle("Not a vehicle")


def test_duplicate_vehicle_id_rejected():
    """Test that duplicate vehicle IDs are rejected."""

    service = VehicleService()

    service.add_vehicle(create_car())

    duplicate_car = Car(
        "CAR-001",
        "Honda",
        "Civic",
        2024,
        4,
        "petrol"
    )

    with pytest.raises(ValueError):
        service.add_vehicle(duplicate_car)


def test_find_vehicle_by_id():
    """Test vehicle search."""

    service = VehicleService()

    car = create_car()
    service.add_vehicle(car)

    found = service.find_vehicle_by_id("CAR-001")

    assert found is car


def test_find_vehicle_case_insensitive():
    """Test case-insensitive vehicle search."""

    service = VehicleService()

    car = create_car()
    service.add_vehicle(car)

    found = service.find_vehicle_by_id("car-001")

    assert found is car


def test_find_missing_vehicle():
    """Test searching for a nonexistent vehicle."""

    service = VehicleService()

    assert service.find_vehicle_by_id(
        "UNKNOWN"
    ) is None


def test_remove_vehicle():
    """Test vehicle removal."""

    service = VehicleService()

    service.add_vehicle(create_car())

    assert service.get_vehicle_count() == 1

    result = service.remove_vehicle("CAR-001")

    assert result is True
    assert service.get_vehicle_count() == 0
    assert service.find_vehicle_by_id(
        "CAR-001"
    ) is None


def test_remove_missing_vehicle():
    """Test removing a nonexistent vehicle."""

    service = VehicleService()

    result = service.remove_vehicle("UNKNOWN")

    assert result is False


def test_rent_vehicle():
    """Test renting an available vehicle."""

    service = VehicleService()

    car = create_car()
    service.add_vehicle(car)

    assert car.is_available() is True

    result = service.rent_vehicle("CAR-001")

    assert result is True
    assert car.is_available() is False


def test_cannot_rent_already_rented_vehicle():
    """Test that an already rented vehicle cannot be rented again."""

    service = VehicleService()

    car = create_car()
    service.add_vehicle(car)

    service.rent_vehicle("CAR-001")

    result = service.rent_vehicle("CAR-001")

    assert result is False


def test_rent_missing_vehicle():
    """Test renting a nonexistent vehicle."""

    service = VehicleService()

    result = service.rent_vehicle("UNKNOWN")

    assert result is False


def test_return_vehicle():
    """Test returning a rented vehicle."""

    service = VehicleService()

    car = create_car()
    service.add_vehicle(car)

    service.rent_vehicle("CAR-001")

    assert car.is_available() is False

    result = service.return_vehicle("CAR-001")

    assert result is True
    assert car.is_available() is True


def test_cannot_return_available_vehicle():
    """Test returning a vehicle that is not rented."""

    service = VehicleService()

    car = create_car()
    service.add_vehicle(car)

    result = service.return_vehicle("CAR-001")

    assert result is False


def test_available_vehicles():
    """Test retrieving available vehicles."""

    service = VehicleService()

    car = create_car()
    motorcycle = create_motorcycle()

    service.add_vehicle(car)
    service.add_vehicle(motorcycle)

    service.rent_vehicle("CAR-001")

    available = service.get_available_vehicles()

    assert len(available) == 1
    assert motorcycle in available
    assert car not in available


def test_rented_vehicles():
    """Test retrieving rented vehicles."""

    service = VehicleService()

    car = create_car()
    motorcycle = create_motorcycle()

    service.add_vehicle(car)
    service.add_vehicle(motorcycle)

    service.rent_vehicle("CAR-001")

    rented = service.get_rented_vehicles()

    assert len(rented) == 1
    assert car in rented
    assert motorcycle not in rented


def test_vehicle_statistics():
    """Test vehicle statistics."""

    service = VehicleService()

    service.add_vehicle(create_car())
    service.add_vehicle(create_motorcycle())
    service.add_vehicle(create_truck())

    service.rent_vehicle("CAR-001")

    statistics = service.get_vehicle_statistics()

    assert statistics["total"] == 3
    assert statistics["cars"] == 1
    assert statistics["motorcycles"] == 1
    assert statistics["trucks"] == 1
    assert statistics["available"] == 2
    assert statistics["rented"] == 1


def test_set_vehicle_availability():
    """Test directly setting vehicle availability."""

    service = VehicleService()

    car = create_car()
    service.add_vehicle(car)

    result = service.set_vehicle_availability(
        "CAR-001",
        False
    )

    assert result is True
    assert car.is_available() is False


def test_set_availability_missing_vehicle():
    """Test availability update for missing vehicle."""

    service = VehicleService()

    result = service.set_vehicle_availability(
        "UNKNOWN",
        False
    )

    assert result is False


def test_get_all_vehicles_returns_copy():
    """Test that get_all_vehicles protects the internal list."""

    service = VehicleService()

    car = create_car()
    service.add_vehicle(car)

    vehicles = service.get_all_vehicles()

    vehicles.clear()

    assert service.get_vehicle_count() == 1


def test_update_common_vehicle_fields():
    """Test updating common vehicle information."""

    service = VehicleService()

    car = create_car()
    service.add_vehicle(car)

    result = service.update_vehicle(
        "CAR-001",
        make="Honda",
        model="Civic",
        year=2024
    )

    assert result is True
    assert car.get_make() == "Honda"
    assert car.get_model() == "Civic"
    assert car.get_year() == 2024


def test_update_car_specific_fields():
    """Test updating Car-specific fields."""

    service = VehicleService()

    car = create_car()
    service.add_vehicle(car)

    service.update_vehicle(
        "CAR-001",
        number_of_doors=2,
        fuel_type="electric"
    )

    assert car.get_number_of_doors() == 2
    assert car.get_fuel_type() == "electric"


def test_update_motorcycle_specific_fields():
    """Test updating Motorcycle-specific fields."""

    service = VehicleService()

    motorcycle = create_motorcycle()
    service.add_vehicle(motorcycle)

    service.update_vehicle(
        "MOTO-001",
        number_of_wheels=3,
        motorcycle_type="cruiser"
    )

    assert motorcycle.get_number_of_wheels() == 3
    assert motorcycle.get_motorcycle_type() == "cruiser"


def test_update_truck_specific_fields():
    """Test updating Truck-specific fields."""

    service = VehicleService()

    truck = create_truck()
    service.add_vehicle(truck)

    service.update_vehicle(
        "TRK-001",
        cargo_capacity=40,
        transmission_type="manual"
    )

    assert truck.get_cargo_capacity() == 40.0
    assert truck.get_transmission_type() == "manual"


def test_update_missing_vehicle():
    """Test updating a nonexistent vehicle."""

    service = VehicleService()

    result = service.update_vehicle(
        "UNKNOWN",
        make="Honda"
    )

    assert result is False


def test_update_invalid_field():
    """Test rejection of unsupported update fields."""

    service = VehicleService()

    service.add_vehicle(create_car())

    with pytest.raises(ValueError):
        service.update_vehicle(
            "CAR-001",
            color="red"
        )