"""
Automated tests for VehicleRepository.
"""
import pytest

from app.exceptions import RepositoryError
from app.models.car import Car
from app.models.motorcycle import Motorcycle
from app.models.truck import Truck
from app.repositories.vehicle_repository import VehicleRepository


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


def test_repository_creates_database(tmp_path):
    """Test database creation."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    assert database.exists()


def test_save_and_get_car(tmp_path):
    """Test saving and retrieving a car."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    car = create_car()

    repository.save_vehicle(car)

    found = repository.get_vehicle_by_id("CAR-001")

    assert found is not None
    assert found.get_vehicle_id() == "CAR-001"
    assert found.get_make() == "Toyota"
    assert found.get_model() == "Corolla"
    assert found.get_number_of_doors() == 4
    assert found.get_fuel_type() == "petrol"


def test_save_and_get_motorcycle(tmp_path):
    """Test saving and retrieving a motorcycle."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    motorcycle = create_motorcycle()

    repository.save_vehicle(motorcycle)

    found = repository.get_vehicle_by_id("MOTO-001")

    assert found is not None
    assert found.get_vehicle_id() == "MOTO-001"
    assert found.get_make() == "Yamaha"
    assert found.get_motorcycle_type() == "sport"


def test_save_and_get_truck(tmp_path):
    """Test saving and retrieving a truck."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    truck = create_truck()

    repository.save_vehicle(truck)

    found = repository.get_vehicle_by_id("TRK-001")

    assert found is not None
    assert found.get_vehicle_id() == "TRK-001"
    assert found.get_make() == "Volvo"
    assert found.get_cargo_capacity() == 25.0


def test_get_all_vehicles(tmp_path):
    """Test retrieving all vehicles."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    repository.save_vehicle(create_car())
    repository.save_vehicle(create_motorcycle())
    repository.save_vehicle(create_truck())

    vehicles = repository.get_all_vehicles()

    assert len(vehicles) == 3


def test_update_vehicle(tmp_path):
    """Test updating a vehicle in the database."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    car = create_car()

    repository.save_vehicle(car)

    car.set_make("Honda")
    car.set_model("Civic")
    car.set_year(2024)
    car.set_fuel_type("electric")

    repository.update_vehicle(car)

    updated = repository.get_vehicle_by_id("CAR-001")

    assert updated.get_make() == "Honda"
    assert updated.get_model() == "Civic"
    assert updated.get_year() == 2024
    assert updated.get_fuel_type() == "electric"


def test_delete_vehicle(tmp_path):
    """Test deleting a vehicle."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    repository.save_vehicle(create_car())

    result = repository.delete_vehicle("CAR-001")

    assert result is True
    assert repository.get_vehicle_by_id("CAR-001") is None


def test_delete_missing_vehicle(tmp_path):
    """Test deleting a nonexistent vehicle."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    result = repository.delete_vehicle("UNKNOWN")

    assert result is False


def test_availability_persists(tmp_path):
    """Test that availability is saved."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    car = create_car()
    car.set_availability(False)

    repository.save_vehicle(car)

    found = repository.get_vehicle_by_id("CAR-001")

    assert found.is_available() is False


def test_duplicate_vehicle_id_raises_repository_error(tmp_path):
    """Test duplicate IDs are rejected by the repository."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    repository.save_vehicle(create_car())

    duplicate = Car(
        "CAR-001",
        "Honda",
        "Civic",
        2024,
        4,
        "petrol"
    )

    with pytest.raises(RepositoryError):
        repository.save_vehicle(duplicate)


def test_clear_all_vehicles(tmp_path):
    """Test clearing the database."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    repository.save_vehicle(create_car())
    repository.save_vehicle(create_motorcycle())

    assert len(repository.get_all_vehicles()) == 2

    repository.clear_all_vehicles()

    assert repository.get_all_vehicles() == []


def test_update_missing_vehicle_raises_error(tmp_path):
    """Test updating a vehicle that doesn't exist."""

    database = tmp_path / "test.db"

    repository = VehicleRepository(str(database))

    car = create_car()

    with pytest.raises(RepositoryError):
        repository.update_vehicle(car)