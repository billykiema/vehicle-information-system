"""
Automated tests for the Car class.
"""

import pytest

from app.models.car import Car


def create_test_car():
    """Create a standard test car."""
    return Car(
        "CAR-001",
        "Toyota",
        "Corolla",
        2023,
        4,
        "petrol"
    )


def test_car_creation():
    """Test Car creation."""

    car = create_test_car()

    assert car.get_vehicle_id() == "CAR-001"
    assert car.get_make() == "Toyota"
    assert car.get_model() == "Corolla"
    assert car.get_year() == 2023
    assert car.get_number_of_doors() == 4
    assert car.get_fuel_type() == "petrol"
    assert car.is_available() is True


def test_car_setters():
    """Test Car setters."""

    car = create_test_car()

    car.set_number_of_doors(2)
    car.set_fuel_type("electric")

    assert car.get_number_of_doors() == 2
    assert car.get_fuel_type() == "electric"


def test_car_availability():
    """Test Car availability."""

    car = create_test_car()

    assert car.is_available() is True

    car.set_availability(False)

    assert car.is_available() is False

    car.set_availability(True)

    assert car.is_available() is True


def test_car_invalid_vehicle_id():
    """Test invalid vehicle IDs."""

    with pytest.raises(ValueError):
        Car(
            "",
            "Toyota",
            "Corolla",
            2023,
            4,
            "petrol"
        )


def test_car_invalid_doors():
    """Test invalid number of doors."""

    car = create_test_car()

    with pytest.raises(ValueError):
        car.set_number_of_doors(-2)


def test_car_invalid_fuel_type():
    """Test invalid fuel type."""

    car = create_test_car()

    with pytest.raises(ValueError):
        car.set_fuel_type("hydrogen")


def test_car_invalid_availability():
    """Test invalid availability value."""

    car = create_test_car()

    with pytest.raises(ValueError):
        car.set_availability("yes")


def test_car_string_representation():
    """Test Car string representation."""

    car = create_test_car()

    output = str(car)

    assert "CAR-001" in output
    assert "Toyota" in output
    assert "Corolla" in output
    assert "2023" in output
    assert "Available" in output