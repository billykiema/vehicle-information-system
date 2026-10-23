"""
Vehicle Interface

Defines the common behavior required by all vehicles.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Base interface for all vehicle types."""
    

    @abstractmethod
    def get_vehicle_id(self) -> str:
        """Return the vehicle ID."""
        pass

    @abstractmethod
    def get_make(self) -> str:
        """Return the vehicle make."""
        pass

    @abstractmethod
    def set_make(self, make: str) -> None:
        """Update the vehicle make."""
        pass

    @abstractmethod
    def get_model(self) -> str:
        """Return the vehicle model."""
        pass

    @abstractmethod
    def set_model(self, model: str) -> None:
        """Update the vehicle model."""
        pass

    @abstractmethod
    def get_year(self) -> int:
        """Return the vehicle manufacturing year."""
        pass

    @abstractmethod
    def set_year(self, year: int) -> None:
        """Update the vehicle manufacturing year."""
        pass
   
    @abstractmethod
    def is_available(self) -> bool:
        """Return True if the vehicle is available."""
        pass

    @abstractmethod
    def set_availability(self, available: bool) -> None:
        """Update vehicle availability."""
        pass
    @abstractmethod
    def get_daily_rate(self) -> float:
                pass
        
    @abstractmethod
    def set_daily_rate(self, daily_rate: float) -> None:
               pass