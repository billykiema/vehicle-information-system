"""
Motorcycle Model

Represents a motorcycle in the Vehicle Information System.
"""

from app.interfaces.vehicle import Vehicle
from app.interfaces.motor_vehicle import MotorVehicle


class Motorcycle(Vehicle, MotorVehicle):
    """Represents a motorcycle in the vehicle information system."""

    VALID_MOTORCYCLE_TYPES = {
        "sport",
        "cruiser",
        "off-road"
    }

    def __init__(
        self,
        vehicle_id: str,
        make: str,
        model: str,
        year: int,
        number_of_wheels: int,
        motorcycle_type: str,
        daily_rate=2500.0
        
    ):
        """Initialize a Motorcycle."""

        self._vehicle_id = self._validate_vehicle_id(vehicle_id)
        self._make = self._validate_text(make, "Make")
        self._model = self._validate_text(model, "Model")
        self._year = self._validate_year(year)

        self.set_number_of_wheels(number_of_wheels)
        self.set_motorcycle_type(motorcycle_type)

        self._available = True

    def get_vehicle_id(self) -> str:
        """Return the vehicle ID."""
        return self._vehicle_id

    def get_make(self) -> str:
        """Return the motorcycle make."""
        return self._make

    def set_make(self, make: str) -> None:
        """Update the motorcycle make."""
        self._make = self._validate_text(make, "Make")

    def get_model(self) -> str:
        """Return the motorcycle model."""
        return self._model

    def set_model(self, model: str) -> None:
        """Update the motorcycle model."""
        self._model = self._validate_text(model, "Model")

    def get_year(self) -> int:
        """Return the motorcycle manufacturing year."""
        return self._year

    def set_year(self, year: int) -> None:
        """Update the motorcycle manufacturing year."""
        self._year = self._validate_year(year)

    def is_available(self) -> bool:
        """Return True if the motorcycle is available."""
        return self._available

    def set_availability(self, available: bool) -> None:
        """Set the motorcycle availability."""

        if not isinstance(available, bool):
            raise ValueError(
                "Availability must be True or False."
            )

        self._available = available
    def get_daily_rate(self) -> float:
        return self._daily_rate
    def set_daily_rate(self, daily_rate: float) -> None:
        if daily_rate <= 0:
            raise ValueError(
            "Daily rental rate must be greater than zero."
        )

        self._daily_rate = float(daily_rate)

    def get_number_of_wheels(self) -> int:
        """Return the number of wheels."""
        return self._number_of_wheels

    def set_number_of_wheels(self, wheels: int) -> None:
        """Set the number of wheels."""

        if isinstance(wheels, bool) or not isinstance(wheels, int):
            raise ValueError(
                "Number of wheels must be an integer."
            )

        if wheels <= 0:
            raise ValueError(
                "Number of wheels must be greater than zero."
            )

        self._number_of_wheels = wheels

    def get_motorcycle_type(self) -> str:
        """Return the motorcycle type."""
        return self._motorcycle_type

    def set_motorcycle_type(
        self,
        motorcycle_type: str
    ) -> None:
        """Set the motorcycle type."""

        if not isinstance(motorcycle_type, str):
            raise ValueError(
                "Motorcycle type must be text."
            )

        motorcycle_type = motorcycle_type.strip().lower()

        if motorcycle_type not in self.VALID_MOTORCYCLE_TYPES:
            raise ValueError(
                "Motorcycle type must be sport, cruiser, or off-road."
            )

        self._motorcycle_type = motorcycle_type

    @staticmethod
    def _validate_vehicle_id(vehicle_id: str) -> str:
        """Validate and normalize the vehicle ID."""

        if not isinstance(vehicle_id, str) or not vehicle_id.strip():
            raise ValueError(
                "Vehicle ID cannot be empty."
            )

        return vehicle_id.strip().upper()

    @staticmethod
    def _validate_text(
        value: str,
        field_name: str
    ) -> str:
        """Validate a text field."""

        if not isinstance(value, str) or not value.strip():
            raise ValueError(
                f"{field_name} cannot be empty."
            )

        return value.strip()

    @staticmethod
    def _validate_year(year: int) -> int:
        """Validate the manufacturing year."""

        if isinstance(year, bool) or not isinstance(year, int):
            raise ValueError(
                "Year must be an integer."
            )

        if year < 1886:
            raise ValueError(
                "Year must be 1886 or later."
            )

        return year

    def __str__(self) -> str:
        """Return a readable motorcycle description."""

        availability = (
            "Available"
            if self._available
            else "Rented"
        )

        return (
            "\n--- Motorcycle Information ---\n"
            f"Vehicle ID: {self._vehicle_id}\n"
            f"Make: {self._make}\n"
            f"Model: {self._model}\n"
            f"Year: {self._year}\n"
            f"Number of Wheels: {self._number_of_wheels}\n"
            f"Motorcycle Type: {self._motorcycle_type}\n"
            f"Availability: {availability}"
        )