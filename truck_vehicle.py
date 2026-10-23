from abc import ABC, abstractmethod


class TruckVehicle(ABC):
    """Interface defining truck-specific behavior."""

    @abstractmethod
    def get_cargo_capacity(self) -> float:
        pass

    @abstractmethod
    def set_cargo_capacity(self, tons: float) -> None:
        pass

    @abstractmethod
    def get_transmission_type(self) -> str:
        pass

    @abstractmethod
    def set_transmission_type(self, transmission_type: str) -> None:
        pass