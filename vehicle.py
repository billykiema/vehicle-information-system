from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Base interface for all vehicles."""

    @abstractmethod
    def get_make(self) -> str:
        pass

    @abstractmethod
    def get_model(self) -> str:
        pass

    @abstractmethod
    def get_year(self) -> int:
        pass