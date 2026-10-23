from vehicle import Vehicle
from car_vehicle import CarVehicle


class Car(Vehicle, CarVehicle):
    """Represents a car."""

    VALID_FUEL_TYPES = {"petrol", "diesel", "electric"}

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        number_of_doors: int,
        fuel_type: str
    ):
        self._make = self._validate_text(make, "Make")
        self._model = self._validate_text(model, "Model")
        self._year = self._validate_year(year)

        self.set_number_of_doors(number_of_doors)
        self.set_fuel_type(fuel_type)

    def get_make(self) -> str:
        return self._make

    def get_model(self) -> str:
        return self._model

    def get_year(self) -> int:
        return self._year

    def get_number_of_doors(self) -> int:
        return self._number_of_doors

    def set_number_of_doors(self, doors: int) -> None:
        if not isinstance(doors, int):
            raise ValueError("Number of doors must be an integer.")

        if doors <= 0:
            raise ValueError(
                "Number of doors must be greater than zero."
            )

        self._number_of_doors = doors

    def get_fuel_type(self) -> str:
        return self._fuel_type

    def set_fuel_type(self, fuel_type: str) -> None:
        if not isinstance(fuel_type, str):
            raise ValueError("Fuel type must be text.")

        fuel_type = fuel_type.strip().lower()

        if fuel_type not in self.VALID_FUEL_TYPES:
            raise ValueError(
                "Invalid fuel type. "
                "Choose petrol, diesel, or electric."
            )

        self._fuel_type = fuel_type

    @staticmethod
    def _validate_text(value: str, field_name: str) -> str:
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} cannot be empty.")

        return value.strip()

    @staticmethod
    def _validate_year(year: int) -> int:
        if not isinstance(year, int):
            raise ValueError("Year must be an integer.")

        if year < 1886:
            raise ValueError("Year must be 1886 or later.")

        return year

    def __str__(self) -> str:
        return (
            "\n--- Car Information ---\n"
            f"Make: {self._make}\n"
            f"Model: {self._model}\n"
            f"Year: {self._year}\n"
            f"Number of Doors: {self._number_of_doors}\n"
            f"Fuel Type: {self._fuel_type}"
        )