"""
Application Exceptions

Custom exceptions used by the Vehicle Information System.
"""


class VehicleSystemError(Exception):
    """Base exception for the Vehicle Information System."""


class RepositoryError(VehicleSystemError):
    """Raised when a database operation fails."""


class VehicleNotFoundError(VehicleSystemError):
    """Raised when a requested vehicle cannot be found."""