"""
Console User Interface

Provides the interactive command-line interface
for the Vehicle Information System.
"""

from app.models.car import Car
from app.models.motorcycle import Motorcycle
from app.models.truck import Truck
from app.services.vehicle_service import VehicleService


class ConsoleUI:
    """Handles user interaction through the console."""

    def __init__(self, vehicle_service: VehicleService):
        """Initialize the console interface."""

        self._vehicle_service = vehicle_service

    def run(self) -> None:
        """Start the main application loop."""

        while True:
            self._display_menu()

            choice = input(
                "\nEnter your choice: "
            ).strip()

            try:

                if choice == "1":
                    self._add_car()

                elif choice == "2":
                    self._add_motorcycle()

                elif choice == "3":
                    self._add_truck()

                elif choice == "4":
                    self._vehicle_service.display_all_vehicles()

                elif choice == "5":
                    self._display_statistics()

                elif choice == "6":
                    self._search_vehicle()

                elif choice == "7":
                    self._remove_vehicle()

                elif choice == "8":
                    self._rent_vehicle()

                elif choice == "9":
                    self._return_vehicle()

                elif choice == "10":
                    self._display_available_vehicles()

                elif choice == "11":
                    self._display_rented_vehicles()

                elif choice == "12":
                    self._update_vehicle()

                elif choice == "13":
                    print(
                        "\nThank you for using the "
                        "Vehicle Information System."
                    )
                    break

                else:
                    print(
                        "\nInvalid choice. "
                        "Please select a valid option."
                    )

            except (ValueError, TypeError) as error:
                print(f"\nError: {error}")

            input("\nPress Enter to continue...")

    def _display_menu(self) -> None:
        """Display the main menu."""

        print("\n" + "=" * 60)
        print("       CAR RENTAL AGENCY VEHICLE INFORMATION SYSTEM")
        print("=" * 60)
        print("1. Add Car")
        print("2. Add Motorcycle")
        print("3. Add Truck")
        print("4. Display All Vehicles")
        print("5. Vehicle Statistics")
        print("6. Search Vehicle")
        print("7. Remove Vehicle")
        print("8. Rent Vehicle")
        print("9. Return Vehicle")
        print("10. Display Available Vehicles")
        print("11. Display Rented Vehicles")
        print("12. Update Vehicle")
        print("13. Exit")
        print("=" * 60)

    def _get_required_text(self, prompt: str) -> str:
        """Get a non-empty text value."""

        value = input(prompt).strip()

        if not value:
            raise ValueError(
                "This field cannot be empty."
            )

        return value

    def _get_integer(
        self,
        prompt: str
    ) -> int:
        """Get an integer from the user."""

        value = input(prompt).strip()

        try:
            return int(value)

        except ValueError:
            raise ValueError(
                "Please enter a valid integer."
            )

    def _get_float(
        self,
        prompt: str
    ) -> float:
        """Get a floating-point number."""

        value = input(prompt).strip()

        try:
            return float(value)

        except ValueError:
            raise ValueError(
                "Please enter a valid number."
            )

    def _get_vehicle_id(self) -> str:
        """Get a vehicle ID from the user."""

        return self._get_required_text(
            "Enter Vehicle ID: "
        )

    def _add_car(self) -> None:
        """Collect information and add a car."""

        print("\n--- ADD CAR ---")

        vehicle_id = self._get_vehicle_id()

        make = self._get_required_text(
            "Enter Make: "
        )

        model = self._get_required_text(
            "Enter Model: "
        )

        year = self._get_integer(
            "Enter Year: "
        )

        doors = self._get_integer(
            "Enter Number of Doors: "
        )

        fuel_type = self._get_required_text(
            "Enter Fuel Type "
            "(petrol/diesel/electric): "
        )

        car = Car(
            vehicle_id,
            make,
            model,
            year,
            doors,
            fuel_type
        )

        self._vehicle_service.add_vehicle(car)

        print(
            f"\nCar '{vehicle_id.upper()}' "
            "added successfully."
        )

    def _add_motorcycle(self) -> None:
        """Collect information and add a motorcycle."""

        print("\n--- ADD MOTORCYCLE ---")

        vehicle_id = self._get_vehicle_id()

        make = self._get_required_text(
            "Enter Make: "
        )

        model = self._get_required_text(
            "Enter Model: "
        )

        year = self._get_integer(
            "Enter Year: "
        )

        wheels = self._get_integer(
            "Enter Number of Wheels: "
        )

        motorcycle_type = self._get_required_text(
            "Enter Motorcycle Type "
            "(sport/cruiser/off-road): "
        )

        motorcycle = Motorcycle(
            vehicle_id,
            make,
            model,
            year,
            wheels,
            motorcycle_type
        )

        self._vehicle_service.add_vehicle(
            motorcycle
        )

        print(
            f"\nMotorcycle '{vehicle_id.upper()}' "
            "added successfully."
        )

    def _add_truck(self) -> None:
        """Collect information and add a truck."""

        print("\n--- ADD TRUCK ---")

        vehicle_id = self._get_vehicle_id()

        make = self._get_required_text(
            "Enter Make: "
        )

        model = self._get_required_text(
            "Enter Model: "
        )

        year = self._get_integer(
            "Enter Year: "
        )

        cargo_capacity = self._get_float(
            "Enter Cargo Capacity (tons): "
        )

        transmission = self._get_required_text(
            "Enter Transmission "
            "(manual/automatic): "
        )

        truck = Truck(
            vehicle_id,
            make,
            model,
            year,
            cargo_capacity,
            transmission
        )

        self._vehicle_service.add_vehicle(truck)

        print(
            f"\nTruck '{vehicle_id.upper()}' "
            "added successfully."
        )

    def _display_statistics(self) -> None:
        """Display vehicle statistics."""

        statistics = (
            self._vehicle_service
            .get_vehicle_statistics()
        )

        print("\n" + "=" * 60)
        print("                 VEHICLE STATISTICS")
        print("=" * 60)

        print(
            f"Total Vehicles: "
            f"{statistics['total']}"
        )

        print(
            f"Cars: "
            f"{statistics['cars']}"
        )

        print(
            f"Motorcycles: "
            f"{statistics['motorcycles']}"
        )

        print(
            f"Trucks: "
            f"{statistics['trucks']}"
        )

        print(
            f"Available: "
            f"{statistics['available']}"
        )

        print(
            f"Rented: "
            f"{statistics['rented']}"
        )

        print("=" * 60)

    def _search_vehicle(self) -> None:
        """Search for a vehicle by ID."""

        print("\n--- SEARCH VEHICLE ---")

        vehicle_id = self._get_vehicle_id()

        vehicle = (
            self._vehicle_service
            .find_vehicle_by_id(vehicle_id)
        )

        if vehicle is None:
            print(
                f"\nNo vehicle found with ID "
                f"'{vehicle_id.upper()}'."
            )
            return

        print("\nVehicle found:")
        print(vehicle)

    def _remove_vehicle(self) -> None:
        """Remove a vehicle by ID."""

        print("\n--- REMOVE VEHICLE ---")

        vehicle_id = self._get_vehicle_id()

        vehicle = (
            self._vehicle_service
            .find_vehicle_by_id(vehicle_id)
        )

        if vehicle is None:
            print(
                f"\nNo vehicle found with ID "
                f"'{vehicle_id.upper()}'."
            )
            return

        print("\nVehicle to be removed:")
        print(vehicle)

        confirmation = input(
            "\nAre you sure you want to remove "
            "this vehicle? (yes/no): "
        ).strip().lower()

        if confirmation != "yes":
            print("\nVehicle removal cancelled.")
            return

        removed = (
            self._vehicle_service
            .remove_vehicle(vehicle_id)
        )

        if removed:
            print("\nVehicle removed successfully.")

    def _rent_vehicle(self) -> None:
        """Rent an available vehicle."""

        print("\n--- RENT VEHICLE ---")

        vehicle_id = self._get_vehicle_id()

        vehicle = (
            self._vehicle_service
            .find_vehicle_by_id(vehicle_id)
        )

        if vehicle is None:
            print(
                f"\nNo vehicle found with ID "
                f"'{vehicle_id.upper()}'."
            )
            return

        if not vehicle.is_available():
            print("\nThis vehicle is already rented.")
            return

        self._vehicle_service.rent_vehicle(
            vehicle_id
        )

        print(
            f"\nVehicle '{vehicle_id.upper()}' "
            "has been rented successfully."
        )

    def _return_vehicle(self) -> None:
        """Return a rented vehicle."""

        print("\n--- RETURN VEHICLE ---")

        vehicle_id = self._get_vehicle_id()

        vehicle = (
            self._vehicle_service
            .find_vehicle_by_id(vehicle_id)
        )

        if vehicle is None:
            print(
                f"\nNo vehicle found with ID "
                f"'{vehicle_id.upper()}'."
            )
            return

        if vehicle.is_available():
            print("\nThis vehicle is not currently rented.")
            return

        self._vehicle_service.return_vehicle(
            vehicle_id
        )

        print(
            f"\nVehicle '{vehicle_id.upper()}' "
            "has been returned successfully."
        )

    def _display_available_vehicles(self) -> None:
        """Display available vehicles."""

        self._vehicle_service.display_available_vehicles()

    def _display_rented_vehicles(self) -> None:
        """Display rented vehicles."""

        self._vehicle_service.display_rented_vehicles()

    def _update_vehicle(self) -> None:
        """Update vehicle information."""

        print("\n--- UPDATE VEHICLE ---")

        vehicle_id = self._get_vehicle_id()

        vehicle = (
            self._vehicle_service
            .find_vehicle_by_id(vehicle_id)
        )

        if vehicle is None:
            print(
                f"\nNo vehicle found with ID "
                f"'{vehicle_id.upper()}'."
            )
            return

        print("\nCurrent vehicle information:")
        print(vehicle)

        print("\nWhat would you like to update?")
        print("1. Make")
        print("2. Model")
        print("3. Year")

        class_name = vehicle.__class__.__name__

        if class_name == "Car":
            print("4. Number of Doors")
            print("5. Fuel Type")

        elif class_name == "Motorcycle":
            print("4. Number of Wheels")
            print("5. Motorcycle Type")

        elif class_name == "Truck":
            print("4. Cargo Capacity")
            print("5. Transmission Type")

        print("6. Availability")
        print("0. Cancel")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        updates = {}

        if choice == "1":
            updates["make"] = self._get_required_text(
                "Enter new Make: "
            )

        elif choice == "2":
            updates["model"] = self._get_required_text(
                "Enter new Model: "
            )

        elif choice == "3":
            updates["year"] = self._get_integer(
                "Enter new Year: "
            )

        elif choice == "4":

            if class_name == "Car":
                updates["number_of_doors"] = (
                    self._get_integer(
                        "Enter new Number of Doors: "
                    )
                )

            elif class_name == "Motorcycle":
                updates["number_of_wheels"] = (
                    self._get_integer(
                        "Enter new Number of Wheels: "
                    )
                )

            elif class_name == "Truck":
                updates["cargo_capacity"] = (
                    self._get_float(
                        "Enter new Cargo Capacity: "
                    )
                )

        elif choice == "5":

            if class_name == "Car":
                updates["fuel_type"] = (
                    self._get_required_text(
                        "Enter new Fuel Type: "
                    )
                )

            elif class_name == "Motorcycle":
                updates["motorcycle_type"] = (
                    self._get_required_text(
                        "Enter new Motorcycle Type: "
                    )
                )

            elif class_name == "Truck":
                updates["transmission_type"] = (
                    self._get_required_text(
                        "Enter new Transmission Type: "
                    )
                )

        elif choice == "6":
            availability = input(
                "Make vehicle available? "
                "(yes/no): "
            ).strip().lower()

            if availability == "yes":
                updates["availability"] = True

            elif availability == "no":
                updates["availability"] = False

            else:
                raise ValueError(
                    "Please enter yes or no."
                )

        elif choice == "0":
            print("\nUpdate cancelled.")
            return

        else:
            print("\nInvalid update option.")
            return

        self._vehicle_service.update_vehicle(
            vehicle_id,
            **updates
        )

        print("\nVehicle updated successfully.")

        updated_vehicle = (
            self._vehicle_service
            .find_vehicle_by_id(vehicle_id)
        )

        print(updated_vehicle)