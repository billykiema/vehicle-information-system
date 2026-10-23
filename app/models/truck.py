"""
Truck Model

Represents a truck in the Vehicle Information System.
"""

from app.interfaces.vehicle import Vehicle
from app.interfaces.truck_vehicle import TruckVehicle


class Truck(Vehicle, TruckVehicle):
    """Represents a truck in the vehicle information system."""

    VALID_TRANSMISSIONS = {
        "manual",
        "automatic"
    }

    def __init__(
        self,
        vehicle_id: str,
        make: str,
        model: str,
        year: int,
        cargo_capacity: float,
        transmission_type: str,
        daily_rate: float = 10000.0,
    ):
        """Initialize a Truck."""

        self._vehicle_id = self._validate_vehicle_id(vehicle_id)
        self._make = self._validate_text(make, "Make")
        self._model = self._validate_text(model, "Model")
        self._year = self._validate_year(year)

        self.set_cargo_capacity(cargo_capacity)
        self.set_transmission_type(transmission_type)
        self.set_daily_rate(daily_rate)

        # Rental availability
        self._available = True

    def get_daily_rate(self) -> float:
        """Return the daily rental rate for this truck."""
        return self._daily_rate

    def set_daily_rate(self, daily_rate: float) -> None:
        """Update the daily rental rate for this truck."""
        if daily_rate <= 0:
            raise ValueError(
                "Daily rental rate must be greater than zero."
            )
        self._daily_rate = float(daily_rate)

    def get_vehicle_id(self) -> str:
        """Return the unique vehicle ID."""
        return self._vehicle_id

    def is_available(self) -> bool:
        """Return True if the truck is available for rental."""
        return self._available

    def set_availability(self, available: bool) -> None:
        """Set the truck availability status."""

        if not isinstance(available, bool):
            raise ValueError(
                "Availability must be True or False."
            )

        self._available = available

    def get_make(self) -> str:
        """Return the truck make."""
        return self._make

    def set_make(self, make: str) -> None:
        """Update the truck make."""
        self._make = self._validate_text(make, "Make")

    def get_model(self) -> str:
        """Return the truck model."""
        return self._model

    def set_model(self, model: str) -> None:
        """Update the truck model."""
        self._model = self._validate_text(model, "Model")

    def get_year(self) -> int:
        """Return the truck manufacturing year."""
        return self._year

    def set_year(self, year: int) -> None:
        """Update the truck manufacturing year."""
        self._year = self._validate_year(year)

    def get_cargo_capacity(self) -> float:
        """Return the cargo capacity in tons."""
        return self._cargo_capacity

    def set_cargo_capacity(self, tons: float) -> None:
        """Set the truck cargo capacity."""

        if isinstance(tons, bool) or not isinstance(
            tons, (int, float)
        ):
            raise ValueError(
                "Cargo capacity must be a number."
            )

        if tons <= 0:
            raise ValueError(
                "Cargo capacity must be greater than zero."
            )

        self._cargo_capacity = float(tons)

    def get_transmission_type(self) -> str:
        """Return the transmission type."""
        return self._transmission_type

    def set_transmission_type(
        self,
        transmission_type: str
    ) -> None:
        """Set the truck transmission type."""

        if not isinstance(transmission_type, str):
            raise ValueError(
                "Transmission type must be text."
            )

        transmission_type = (
            transmission_type.strip().lower()
        )

        if transmission_type not in self.VALID_TRANSMISSIONS:
            raise ValueError(
                "Invalid transmission type. "
                "Choose manual or automatic."
            )

        self._transmission_type = transmission_type

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
        """Return a readable truck description."""

        availability = (
            "Available"
            if self._available
            else "Rented"
        )

        return (
            "\n--- Truck Information ---\n"
            f"Vehicle ID: {self._vehicle_id}\n"
            f"Make: {self._make}\n"
            f"Model: {self._model}\n"
            f"Year: {self._year}\n"
            f"Cargo Capacity: "
            f"{self._cargo_capacity:.2f} tons\n"
            f"Transmission: {self._transmission_type}\n"
            f"Daily Rate: ${self._daily_rate:.2f}\n"
            f"Availability: {availability}"
        )