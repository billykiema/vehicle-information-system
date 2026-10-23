from abc import ABC, abstractmethod


class MotorVehicle(ABC):
    """Interface defining motorcycle-specific behavior."""

    @abstractmethod
    def get_number_of_wheels(self) -> int:
        pass

    @abstractmethod
    def set_number_of_wheels(self, wheels: int) -> None:
        pass

    @abstractmethod
    def get_motorcycle_type(self) -> str:
        pass

    @abstractmethod
    def set_motorcycle_type(self, motorcycle_type: str) -> None:
        pass