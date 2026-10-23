"""
Vehicle Service Module

Provides business logic for managing vehicles
in the rental system.
"""

from app.interfaces.vehicle import Vehicle
from app.repositories.vehicle_repository import VehicleRepository
from app.exceptions import VehicleNotFoundError


class VehicleService:
    """Manages vehicles and coordinates database persistence."""

    def __init__(
        self,
        repository: VehicleRepository | None = None
    ):
        """
        Initialize the vehicle service.

        A repository can be supplied to enable database persistence.
        If no repository is supplied, the service operates in memory.
        """

        self._vehicles: list[Vehicle] = []
        self._repository = repository

        # Load existing vehicles from the database.
        if self._repository is not None:
            self._vehicles = self._repository.get_all_vehicles()

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """
        Add a valid vehicle.

        Vehicle IDs must be unique.
        """

        if not isinstance(vehicle, Vehicle):
            raise TypeError(
                "Only objects implementing the Vehicle "
                "interface can be added."
            )

        if self.find_vehicle_by_id(
            vehicle.get_vehicle_id()
        ) is not None:
            raise ValueError(
                f"Vehicle ID '{vehicle.get_vehicle_id()}' "
                "already exists."
            )

        self._vehicles.append(vehicle)

        # Persist the new vehicle.
        if self._repository is not None:
            self._repository.save_vehicle(vehicle)

    def get_all_vehicles(self) -> list[Vehicle]:
        """Return a copy of all registered vehicles."""
        return self._vehicles.copy()

    def get_vehicle_count(self) -> int:
        """Return the total number of registered vehicles."""
        return len(self._vehicles)

    def find_vehicle_by_id(
        self,
        vehicle_id: str
    ) -> Vehicle | None:
        """Find a vehicle by ID."""

        if not isinstance(vehicle_id, str):
            return None

        vehicle_id = vehicle_id.strip().upper()

        for vehicle in self._vehicles:
            if vehicle.get_vehicle_id() == vehicle_id:
                return vehicle

        return None

    def remove_vehicle(self, vehicle_id: str) -> bool:
        """Remove a vehicle by ID."""

        vehicle = self.find_vehicle_by_id(vehicle_id)

        if vehicle is None:
            return False

        self._vehicles.remove(vehicle)

        if self._repository is not None:
            self._repository.delete_vehicle(vehicle_id)

        return True

    def set_vehicle_availability(
        self,
        vehicle_id: str,
        available: bool
    ) -> bool:
        """Change the availability of a vehicle."""

        vehicle = self.find_vehicle_by_id(vehicle_id)

        if vehicle is None:
            return False

        vehicle.set_availability(available)

        if self._repository is not None:
            self._repository.update_vehicle(vehicle)

        return True

    def rent_vehicle(self, vehicle_id):
        """Rent a vehicle by ID. Returns True on success, False otherwise."""

        vehicle = self.find_vehicle_by_id(vehicle_id)

        if vehicle is None:
            return False

        if not vehicle.is_available():
            return False

        vehicle.set_availability(False)

        if self._repository is not None:
            self._repository.update_vehicle(vehicle)

        return True

    def return_vehicle(self, vehicle_id):
        """Return a rented vehicle by ID. Returns True on success, False otherwise."""

        vehicle = self.find_vehicle_by_id(vehicle_id)

        if vehicle is None:
            return False

        if vehicle.is_available():
            return False

        vehicle.set_availability(True)

        if self._repository is not None:
            self._repository.update_vehicle(vehicle)

        return True

    def get_available_vehicles(self) -> list[Vehicle]:
        """Return all vehicles currently available."""

        return [
            vehicle
            for vehicle in self._vehicles
            if vehicle.is_available()
        ]

    def get_rented_vehicles(self) -> list[Vehicle]:
        """Return all vehicles currently rented."""

        return [
            vehicle
            for vehicle in self._vehicles
            if not vehicle.is_available()
        ]

    def get_vehicle_statistics(self) -> dict:
        """Return vehicle statistics."""

        statistics = {
            "total": 0,
            "cars": 0,
            "motorcycles": 0,
            "trucks": 0,
            "available": 0,
            "rented": 0
        }

        statistics["total"] = len(self._vehicles)

        for vehicle in self._vehicles:

            class_name = (
                vehicle.__class__.__name__.lower()
            )

            if class_name == "car":
                statistics["cars"] += 1

            elif class_name == "motorcycle":
                statistics["motorcycles"] += 1

            elif class_name == "truck":
                statistics["trucks"] += 1

            if vehicle.is_available():
                statistics["available"] += 1
            else:
                statistics["rented"] += 1

        return statistics

    def update_vehicle(
        self,
        vehicle_id: str,
        **updates
    ) -> bool:
        """
        Update vehicle information safely.

        All supplied values are validated before the vehicle
        is modified. This prevents partially completed updates.
        """

        vehicle = self.find_vehicle_by_id(vehicle_id)

        if vehicle is None:
            return False

        # Store the original values so they can be restored
        # if persistence fails.
        original_values = {
            "make": vehicle.get_make(),
            "model": vehicle.get_model(),
            "year": vehicle.get_year(),
            "availability": vehicle.is_available()
        }

        if hasattr(vehicle, "get_number_of_doors"):
            original_values["number_of_doors"] = (
                vehicle.get_number_of_doors()
            )

        if hasattr(vehicle, "get_fuel_type"):
            original_values["fuel_type"] = (
                vehicle.get_fuel_type()
            )

        if hasattr(vehicle, "get_number_of_wheels"):
            original_values["number_of_wheels"] = (
                vehicle.get_number_of_wheels()
            )

        if hasattr(vehicle, "get_motorcycle_type"):
            original_values["motorcycle_type"] = (
                vehicle.get_motorcycle_type()
            )

        if hasattr(vehicle, "get_cargo_capacity"):
            original_values["cargo_capacity"] = (
                vehicle.get_cargo_capacity()
            )

        if hasattr(vehicle, "get_transmission_type"):
            original_values["transmission_type"] = (
                vehicle.get_transmission_type()
            )

        try:

            # Apply validated changes.
            for field, value in updates.items():

                if field == "make":
                    vehicle.set_make(value)

                elif field == "model":
                    vehicle.set_model(value)

                elif field == "year":
                    vehicle.set_year(value)

                elif field == "availability":
                    vehicle.set_availability(value)

                elif field == "number_of_doors":

                    if hasattr(
                        vehicle,
                        "set_number_of_doors"
                    ):
                        vehicle.set_number_of_doors(value)

                    else:
                        raise ValueError(
                            "This vehicle does not support "
                            "number of doors."
                        )

                elif field == "fuel_type":

                    if hasattr(
                        vehicle,
                        "set_fuel_type"
                    ):
                        vehicle.set_fuel_type(value)

                    else:
                        raise ValueError(
                            "This vehicle does not support "
                            "fuel type."
                        )

                elif field == "number_of_wheels":

                    if hasattr(
                        vehicle,
                        "set_number_of_wheels"
                    ):
                        vehicle.set_number_of_wheels(value)

                    else:
                        raise ValueError(
                            "This vehicle does not support "
                            "number of wheels."
                        )

                elif field == "motorcycle_type":

                    if hasattr(
                        vehicle,
                        "set_motorcycle_type"
                    ):
                        vehicle.set_motorcycle_type(value)

                    else:
                        raise ValueError(
                            "This vehicle does not support "
                            "motorcycle type."
                        )

                elif field == "cargo_capacity":

                    if hasattr(
                        vehicle,
                        "set_cargo_capacity"
                    ):
                        vehicle.set_cargo_capacity(value)

                    else:
                        raise ValueError(
                            "This vehicle does not support "
                            "cargo capacity."
                        )

                elif field == "transmission_type":

                    if hasattr(
                        vehicle,
                        "set_transmission_type"
                    ):
                        vehicle.set_transmission_type(value)

                    else:
                        raise ValueError(
                            "This vehicle does not support "
                            "transmission type."
                        )

                else:

                    raise ValueError(
                        f"Unsupported vehicle field: {field}"
                    )

            # Persist only after every update succeeds.
            if self._repository is not None:
                self._repository.update_vehicle(
                    vehicle
                )

            return True

        except Exception:

            # Restore the original in-memory values.
            vehicle.set_make(
                original_values["make"]
            )

            vehicle.set_model(
                original_values["model"]
            )

            vehicle.set_year(
                original_values["year"]
            )

            vehicle.set_availability(
                original_values["availability"]
            )

            if "number_of_doors" in original_values:
                vehicle.set_number_of_doors(
                    original_values["number_of_doors"]
                )

            if "fuel_type" in original_values:
                vehicle.set_fuel_type(
                    original_values["fuel_type"]
                )

            if "number_of_wheels" in original_values:
                vehicle.set_number_of_wheels(
                    original_values["number_of_wheels"]
                )

            if "motorcycle_type" in original_values:
                vehicle.set_motorcycle_type(
                    original_values["motorcycle_type"]
                )

            if "cargo_capacity" in original_values:
                vehicle.set_cargo_capacity(
                    original_values["cargo_capacity"]
                )

            if "transmission_type" in original_values:
                vehicle.set_transmission_type(
                    original_values["transmission_type"]
                )

            raise

    def display_all_vehicles(self) -> None:
        """Display all registered vehicles."""

        if not self._vehicles:
            print("\nNo vehicles have been registered.")
            return

        print("\n" + "=" * 60)
        print("               ALL REGISTERED VEHICLES")
        print("=" * 60)

        for number, vehicle in enumerate(
            self._vehicles,
            start=1
        ):
            print(f"\nVehicle #{number}")
            print(vehicle)

        print("=" * 60)

    def display_available_vehicles(self) -> None:
        """Display vehicles currently available."""

        vehicles = self.get_available_vehicles()

        if not vehicles:
            print("\nNo vehicles are currently available.")
            return

        print("\n" + "=" * 60)
        print("                 AVAILABLE VEHICLES")
        print("=" * 60)

        for number, vehicle in enumerate(
            vehicles,
            start=1
        ):
            print(f"\nVehicle #{number}")
            print(vehicle)

        print("=" * 60)

    def display_rented_vehicles(self) -> None:
        """Display vehicles currently rented."""

        vehicles = self.get_rented_vehicles()

        if not vehicles:
            print("\nNo vehicles are currently rented.")
            return

        print("\n" + "=" * 60)
        print("                  RENTED VEHICLES")
        print("=" * 60)

        for number, vehicle in enumerate(
            vehicles,
            start=1
        ):
            print(f"\nVehicle #{number}")
            print(vehicle)

        print("=" * 60)
