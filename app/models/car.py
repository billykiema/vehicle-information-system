"""
Car Model

Represents a car in the Vehicle Information System.
"""

from app.interfaces.vehicle import Vehicle
from app.interfaces.car_vehicle import CarVehicle


class Car(Vehicle, CarVehicle):
    """Represents a car in the vehicle information system."""

    VALID_FUEL_TYPES = {
        "petrol",
        "diesel",
        "electric"
    }

    def __init__(
        self,
        vehicle_id: str,
        make: str,
        model: str,
        year: int,
        number_of_doors: int,
        fuel_type: str,
        daily_rate = 5000.0
    ):
        """Initialize a Car."""

        self._vehicle_id = self._validate_vehicle_id(vehicle_id)
        self._make = self._validate_text(make, "Make")
        self._model = self._validate_text(model, "Model")
        self._year = self._validate_year(year)
        self._daily_rate = float(daily_rate)

        self.set_number_of_doors(number_of_doors)
        self.set_daily_rate(daily_rate)
        self.set_fuel_type(fuel_type)

        # New rental-system property
        self._available = True

    # ---------------------------------------------------------
    # Vehicle identification
    # ---------------------------------------------------------

    def get_vehicle_id(self) -> str:
        """Return the unique vehicle ID."""
        return self._vehicle_id

    # ---------------------------------------------------------
    # Availability
    # ---------------------------------------------------------

    def is_available(self) -> bool:
        """Return True if the car is available for rental."""
        return self._available

    def set_availability(self, available: bool) -> None:
        """Set the availability of the car."""

        if not isinstance(available, bool):
            raise ValueError(
                "Availability must be True or False."
            )

        self._available = available

    # ---------------------------------------------------------
    # Basic vehicle information
    # ---------------------------------------------------------

    def get_make(self) -> str:
        """Return the vehicle make."""
        return self._make
    
    def set_make(self, make: str) -> None:
         """Update the car make."""
         self._make = self._validate_text(make, "Make")
         
    

    def get_model(self) -> str:
        """Return the vehicle model."""
        return self._model
    def set_model(self, model: str) -> None:
         """Update the car model."""
         self._model = self._validate_text(model, "Model")

    def get_year(self) -> int:
        """Return the vehicle manufacturing year."""
        return self._year
    def set_year(self, year: int) -> None:
         """Update the car manufacturing year."""
         self._year = self._validate_year(year)
    def get_daily_rate(self) -> float:
        return self._daily_rate

    def set_daily_rate(self, daily_rate: float) -> None:
        if daily_rate <= 0:
            raise ValueError(
            "Daily rental rate must be greater than zero."
         )

        self._daily_rate = float(daily_rate)


    # ---------------------------------------------------------
    # Car-specific information
    # ---------------------------------------------------------

    def get_number_of_doors(self) -> int:
        """Return the number of doors."""
        return self._number_of_doors

    def set_number_of_doors(self, doors: int) -> None:
        """Set the number of doors."""

        if isinstance(doors, bool) or not isinstance(doors, int):
            raise ValueError(
                "Number of doors must be an integer."
            )

        if doors <= 0:
            raise ValueError(
                "Number of doors must be greater than zero."
            )

        self._number_of_doors = doors

    def get_fuel_type(self) -> str:
        """Return the fuel type."""
        return self._fuel_type

    def set_fuel_type(self, fuel_type: str) -> None:
        """Set the fuel type."""

        if not isinstance(fuel_type, str):
            raise ValueError(
                "Fuel type must be text."
            )

        fuel_type = fuel_type.strip().lower()

        if fuel_type not in self.VALID_FUEL_TYPES:
            raise ValueError(
                "Fuel type must be petrol, diesel, or electric."
            )

        self._fuel_type = fuel_type
    def get_daily_rate(self) -> float:
        """Return the daily rental rate for this car."""
        return self._daily_rate

    def set_daily_rate(self, daily_rate: float) -> None:
        """Update the daily rental rate for this car."""
        if daily_rate <= 0:
            raise ValueError("Daily rate must be a positive number.")
        self._daily_rate = float (daily_rate)

    # ---------------------------------------------------------
    # Validation
    # ---------------------------------------------------------

    @staticmethod
    def _validate_vehicle_id(vehicle_id: str) -> str:
        """Validate the vehicle ID."""

        if not isinstance(vehicle_id, str) or not vehicle_id.strip():
            raise ValueError(
                "Vehicle ID cannot be empty."
            )

        return vehicle_id.strip().upper()

    @staticmethod
    def _validate_text(value: str, field_name: str) -> str:
        """Validate text fields."""

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

    # ---------------------------------------------------------
    # String representation
    # ---------------------------------------------------------

    def __str__(self) -> str:
        """Return a readable representation of the car."""

        availability = (
            "Available"
            if self._available
            else "Rented"
        )

        return (
            "\n--- Car Information ---\n"
            f"Vehicle ID: {self._vehicle_id}\n"
            f"Make: {self._make}\n"
            f"Model: {self._model}\n"
            f"Year: {self._year}\n"
            f"Number of Doors: {self._number_of_doors}\n"
            f"Fuel Type: {self._fuel_type}\n"
            f"Availability: {availability}"
        )