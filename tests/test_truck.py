"""
Automated tests for the Truck class.
"""

import pytest

from app.models.truck import Truck


def create_test_truck():
    """Create a standard test truck."""

    return Truck(
        "TRK-001",
        "Volvo",
        "FH16",
        2022,
        25,
        "automatic"
    )


def test_truck_creation():
    """Test Truck creation."""

    truck = create_test_truck()

    assert truck.get_vehicle_id() == "TRK-001"
    assert truck.get_make() == "Volvo"
    assert truck.get_model() == "FH16"
    assert truck.get_year() == 2022
    assert truck.get_cargo_capacity() == 25.0
    assert truck.get_transmission_type() == "automatic"
    assert truck.is_available() is True


def test_truck_setters():
    """Test Truck setters."""

    truck = create_test_truck()

    truck.set_cargo_capacity(30)
    truck.set_transmission_type("manual")

    assert truck.get_cargo_capacity() == 30.0
    assert truck.get_transmission_type() == "manual"


def test_truck_availability():
    """Test Truck availability."""

    truck = create_test_truck()

    assert truck.is_available() is True

    truck.set_availability(False)

    assert truck.is_available() is False

    truck.set_availability(True)

    assert truck.is_available() is True


def test_truck_invalid_vehicle_id():
    """Test invalid vehicle ID."""

    with pytest.raises(ValueError):
        Truck(
            "",
            "Volvo",
            "FH16",
            2022,
            25,
            "automatic"
        )


def test_truck_invalid_capacity():
    """Test that negative cargo capacity is rejected."""

    truck = create_test_truck()

    with pytest.raises(ValueError):
        truck.set_cargo_capacity(-5)


def test_truck_invalid_transmission():
    """Test invalid transmission types."""

    truck = create_test_truck()

    with pytest.raises(ValueError):
        truck.set_transmission_type("semi-automatic")


def test_truck_invalid_availability():
    """Test invalid availability value."""

    truck = create_test_truck()

    with pytest.raises(ValueError):
        truck.set_availability("rented")


def test_truck_string_representation():
    """Test Truck string representation."""

    truck = create_test_truck()

    output = str(truck)

    assert "TRK-001" in output
    assert "Volvo" in output
    assert "FH16" in output
    assert "2022" in output
    assert "Available" in output