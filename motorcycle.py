from vehicle import Vehicle
from motor_vehicle import MotorVehicle


class Motorcycle(Vehicle, MotorVehicle):
    """Represents a motorcycle."""

    VALID_TYPES = {"sport", "cruiser", "off-road"}

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        number_of_wheels: int,
        motorcycle_type: str
    ):
        self._make = self._validate_text(make, "Make")
        self._model = self._validate_text(model, "Model")
        self._year = self._validate_year(year)

        self.set_number_of_wheels(number_of_wheels)
        self.set_motorcycle_type(motorcycle_type)

    def get_make(self) -> str:
        return self._make

    def get_model(self) -> str:
        return self._model

    def get_year(self) -> int:
        return self._year

    def get_number_of_wheels(self) -> int:
        return self._number_of_wheels

    def set_number_of_wheels(self, wheels: int) -> None:
        if not isinstance(wheels, int):
            raise ValueError("Number of wheels must be an integer.")

        if wheels <= 0:
            raise ValueError(
                "Number of wheels must be greater than zero."
            )

        self._number_of_wheels = wheels

    def get_motorcycle_type(self) -> str:
        return self._motorcycle_type

    def set_motorcycle_type(self, motorcycle_type: str) -> None:
        if not isinstance(motorcycle_type, str):
            raise ValueError("Motorcycle type must be text.")

        motorcycle_type = motorcycle_type.strip().lower()

        if motorcycle_type not in self.VALID_TYPES:
            raise ValueError(
                "Invalid motorcycle type. "
                "Choose sport, cruiser, or off-road."
            )

        self._motorcycle_type = motorcycle_type

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
            "\n--- Motorcycle Information ---\n"
            f"Make: {self._make}\n"
            f"Model: {self._model}\n"
            f"Year: {self._year}\n"
            f"Number of Wheels: {self._number_of_wheels}\n"
            f"Motorcycle Type: {self._motorcycle_type}"
        )