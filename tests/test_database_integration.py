"""
Integration tests for the Vehicle Information System.

These tests verify that the service and repository
work together correctly.
"""

from app.models.car import Car
from app.models.motorcycle import Motorcycle
from app.repositories.vehicle_repository import VehicleRepository
from app.services.vehicle_service import VehicleService


def create_car():
    """Create a test car."""

    return Car(
        "CAR-100",
        "Toyota",
        "Camry",
        2024,
        4,
        "petrol"
    )


def test_vehicle_survives_service_restart(tmp_path):
    """
    Test that a vehicle remains available after creating
    a new service instance.
    """

    database = tmp_path / "integration.db"

    repository = VehicleRepository(
        str(database)
    )

    service = VehicleService(repository)

    service.add_vehicle(create_car())

    # Simulate closing and restarting the application.
    new_repository = VehicleRepository(
        str(database)
    )

    new_service = VehicleService(
        new_repository
    )

    vehicle = new_service.find_vehicle_by_id(
        "CAR-100"
    )

    assert vehicle is not None
    assert vehicle.get_make() == "Toyota"
    assert vehicle.get_model() == "Camry"


def test_rental_status_survives_restart(tmp_path):
    """Test rental status persistence."""

    database = tmp_path / "integration.db"

    repository = VehicleRepository(
        str(database)
    )

    service = VehicleService(repository)

    service.add_vehicle(create_car())

    service.rent_vehicle("CAR-100")

    new_repository = VehicleRepository(
        str(database)
    )

    new_service = VehicleService(
        new_repository
    )

    vehicle = new_service.find_vehicle_by_id(
        "CAR-100"
    )

    assert vehicle is not None
    assert vehicle.is_available() is False


def test_return_status_survives_restart(tmp_path):
    """Test returned vehicle persistence."""

    database = tmp_path / "integration.db"

    repository = VehicleRepository(
        str(database)
    )

    service = VehicleService(repository)

    service.add_vehicle(create_car())

    service.rent_vehicle("CAR-100")
    service.return_vehicle("CAR-100")

    new_repository = VehicleRepository(
        str(database)
    )

    new_service = VehicleService(
        new_repository
    )

    vehicle = new_service.find_vehicle_by_id(
        "CAR-100"
    )

    assert vehicle is not None
    assert vehicle.is_available() is True


def test_update_survives_restart(tmp_path):
    """Test vehicle updates survive a restart."""

    database = tmp_path / "integration.db"

    repository = VehicleRepository(
        str(database)
    )

    service = VehicleService(repository)

    service.add_vehicle(create_car())

    service.update_vehicle(
        "CAR-100",
        make="Honda",
        model="Accord",
        year=2025
    )

    new_repository = VehicleRepository(
        str(database)
    )

    new_service = VehicleService(
        new_repository
    )

    vehicle = new_service.find_vehicle_by_id(
        "CAR-100"
    )

    assert vehicle.get_make() == "Honda"
    assert vehicle.get_model() == "Accord"
    assert vehicle.get_year() == 2025


def test_delete_survives_restart(tmp_path):
    """Test vehicle deletion persistence."""

    database = tmp_path / "integration.db"

    repository = VehicleRepository(
        str(database)
    )

    service = VehicleService(repository)

    service.add_vehicle(create_car())

    assert service.remove_vehicle(
        "CAR-100"
    ) is True

    new_repository = VehicleRepository(
        str(database)
    )

    new_service = VehicleService(
        new_repository
    )

    assert new_service.find_vehicle_by_id(
        "CAR-100"
    ) is None