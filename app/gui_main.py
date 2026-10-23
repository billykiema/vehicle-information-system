"""
Graphical entry point for the Vehicle Information System.
"""

from app.repositories.vehicle_repository import VehicleRepository
from app.services.vehicle_service import VehicleService
from app.ui.gui import VehicleGUI
def main():
    repository = VehicleRepository("database/vehicle_rental.db")
    service = VehicleService(repository)
    app = VehicleGUI(service)
    app.run()


if __name__ == "__main__":
    main()