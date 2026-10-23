"""
Automated tests for the Motorcycle class.
"""

import pytest

from app.models.motorcycle import Motorcycle


def create_test_motorcycle():
    """Create a standard test motorcycle."""

    return Motorcycle(
        "MOTO-001",
        "Yamaha",
        "R1",
        2024,
        2,
        "sport"
    )


def test_motorcycle_creation():
    """Test Motorcycle creation."""

    motorcycle = create_test_motorcycle()

    assert motorcycle.get_vehicle_id() == "MOTO-001"
    assert motorcycle.get_make() == "Yamaha"
    assert motorcycle.get_model() == "R1"
    assert motorcycle.get_year() == 2024
    assert motorcycle.get_number_of_wheels() == 2
    assert motorcycle.get_motorcycle_type() == "sport"
    assert motorcycle.is_available() is True


def test_motorcycle_setters():
    """Test Motorcycle setters."""

    motorcycle = create_test_motorcycle()

    motorcycle.set_number_of_wheels(3)
    motorcycle.set_motorcycle_type("cruiser")

    assert motorcycle.get_number_of_wheels() == 3
    assert motorcycle.get_motorcycle_type() == "cruiser"


def test_motorcycle_availability():
    """Test Motorcycle availability."""

    motorcycle = create_test_motorcycle()

    assert motorcycle.is_available() is True

    motorcycle.set_availability(False)

    assert motorcycle.is_available() is False

    motorcycle.set_availability(True)

    assert motorcycle.is_available() is True


def test_motorcycle_invalid_vehicle_id():
    """Test invalid vehicle ID."""

    with pytest.raises(ValueError):
        Motorcycle(
            "",
            "Yamaha",
            "R1",
            2024,
            2,
            "sport"
        )


def test_motorcycle_invalid_wheels():
    """Test invalid number of wheels."""

    motorcycle = create_test_motorcycle()

    with pytest.raises(ValueError):
        motorcycle.set_number_of_wheels(0)


def test_motorcycle_invalid_type():
    """Test invalid motorcycle type."""

    motorcycle = create_test_motorcycle()

    with pytest.raises(ValueError):
        motorcycle.set_motorcycle_type("racing")


def test_motorcycle_invalid_availability():
    """Test invalid availability value."""

    motorcycle = create_test_motorcycle()

    with pytest.raises(ValueError):
        motorcycle.set_availability("available")


def test_motorcycle_string_representation():
    """Test Motorcycle string representation."""

    motorcycle = create_test_motorcycle()

    output = str(motorcycle)

    assert "MOTO-001" in output
    assert "Yamaha" in output
    assert "R1" in output
    assert "2024" in output
    assert "Available" in output