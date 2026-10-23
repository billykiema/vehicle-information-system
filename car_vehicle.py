from abc import ABC, abstractmethod


class CarVehicle(ABC):
    """Interface defining car-specific behavior."""

    @abstractmethod
    def get_number_of_doors(self) -> int:
        pass

    @abstractmethod
    def set_number_of_doors(self, doors: int) -> None:
        pass

    @abstractmethod
    def get_fuel_type(self) -> str:
        pass

    @abstractmethod
    def set_fuel_type(self, fuel_type: str) -> None:
        pass