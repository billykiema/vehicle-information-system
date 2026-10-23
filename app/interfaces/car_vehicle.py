from abc import ABC, abstractmethod


class CarVehicle(ABC):
    """
    Interface defining behavior specific to cars.
    """

    @abstractmethod
    def get_number_of_doors(self) -> int:
        """Return the number of doors."""
        pass

    @abstractmethod
    def set_number_of_doors(self, doors: int) -> None:
        """Set the number of doors."""
        pass

    @abstractmethod
    def get_fuel_type(self) -> str:
        """Return the fuel type."""
        pass

    @abstractmethod
    def set_fuel_type(self, fuel_type: str) -> None:
        """Set the fuel type."""
        pass