from abc import ABC, abstractmethod


class TruckVehicle(ABC):
    """
    Interface defining behavior specific to trucks.
    """

    @abstractmethod
    def get_cargo_capacity(self) -> float:
        """Return cargo capacity in tons."""
        pass

    @abstractmethod
    def set_cargo_capacity(self, tons: float) -> None:
        """Set cargo capacity in tons."""
        pass

    @abstractmethod
    def get_transmission_type(self) -> str:
        """Return the transmission type."""
        pass

    @abstractmethod
    def set_transmission_type(
        self,
        transmission_type: str
    ) -> None:
        """Set the transmission type."""
        pass