"""
Car Rental Agency Vehicle Information System

Main entry point for the application.
"""

from app.repositories.vehicle_repository import VehicleRepository
from app.services.vehicle_service import VehicleService
from app.ui.console_ui import ConsoleUI


def main():
    """Start the Vehicle Information System."""

    # Create the database repository.
    vehicle_repository = VehicleRepository()

    # Create the service with database persistence enabled.
    vehicle_service = VehicleService(
        vehicle_repository
    )

    # Start the console interface.
    user_interface = ConsoleUI(
        vehicle_service
    )

    user_interface.run()


if __name__ == "__main__":
    main()