from abc import ABC, abstractmethod


class MotorVehicle(ABC):
    """
    Interface defining behavior specific to motorcycles.
    """

    @abstractmethod
    def get_number_of_wheels(self) -> int:
        """Return the number of wheels."""
        pass

    @abstractmethod
    def set_number_of_wheels(self, wheels: int) -> None:
        """Set the number of wheels."""
        pass

    @abstractmethod
    def get_motorcycle_type(self) -> str:
        """Return the motorcycle type."""
        pass

    @abstractmethod
    def set_motorcycle_type(self, motorcycle_type: str) -> None:
        """Set the motorcycle type."""
        pass