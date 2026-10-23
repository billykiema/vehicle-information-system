"""
Vehicle Repository Module

Handles persistent storage of vehicles using SQLite.
"""

import sqlite3
from pathlib import Path

from app.exceptions import RepositoryError
from app.models.car import Car
from app.models.motorcycle import Motorcycle
from app.models.truck import Truck


class VehicleRepository:
    """Provides database persistence for vehicles."""

    def __init__(self, database_path: str = "database/vehicle_rental.db"):
        """Initialize the vehicle repository."""

        self._database_path = Path(database_path)

        # Create the database directory if necessary.
        self._database_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        self._create_table()
        self._ensure_daily_rate_column()

    def _connect(self):
        """Create and return a database connection."""

        return sqlite3.connect(self._database_path)

    def _create_table(self) -> None:
        """Create the vehicles table if it does not exist."""

        connection = self._connect()
    
        try:
             connection.execute(
                """
                CREATE TABLE IF NOT EXISTS vehicles (
                    vehicle_id TEXT PRIMARY KEY,
                    vehicle_type TEXT NOT NULL,
                    make TEXT NOT NULL,
                    model TEXT NOT NULL,
                    year INTEGER NOT NULL,
                    number_of_doors INTEGER,
                    fuel_type TEXT,
                    number_of_wheels INTEGER,
                    motorcycle_type TEXT,
                    cargo_capacity REAL,
                    transmission_type TEXT,
                    available INTEGER NOT NULL,
                    daily_rate REAL NOT NULL DEFAULT 5000.0
                )
                """
            )

             connection.commit()

        finally:
             connection.close()
    def _ensure_daily_rate_column(self):
              with self._connect() as connection:
                  cursor = connection.cursor()
     
                  cursor.execute("PRAGMA table_info(vehicles)")
                  columns = [row[1] for row in cursor.fetchall()]
     
                  if "daily_rate" not in columns:
                   cursor.execute(
                     """
                     ALTER TABLE vehicles
                     ADD COLUMN daily_rate REAL NOT NULL DEFAULT 5000.0
                     """
                 )
     
                  connection.commit()
             

    def save_vehicle(self, vehicle) -> None:
        """Save a vehicle to the database."""

        data = self._vehicle_to_record(vehicle)

        connection = self._connect()

        try:
            try:
                connection.execute(
                    """
                    INSERT INTO vehicles (
                        vehicle_id,
                        vehicle_type,
                        make,
                        model,
                        year,
                        number_of_doors,
                        fuel_type,
                        number_of_wheels,
                        motorcycle_type,
                        cargo_capacity,
                        transmission_type,
                        available
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    data
                )

                connection.commit()

            except sqlite3.IntegrityError as error:
                raise RepositoryError(
                    f"Vehicle ID '{vehicle.get_vehicle_id()}' "
                    "already exists."
                ) from error

        finally:
            connection.close()

    def update_vehicle(self, vehicle) -> None:
        """Update an existing vehicle in the database."""

        data = self._vehicle_to_record(vehicle)

        connection = self._connect()

        try:
            cursor = connection.execute(
                """
                UPDATE vehicles
                SET
                    vehicle_type = ?,
                    make = ?,
                    model = ?,
                    year = ?,
                    number_of_doors = ?,
                    fuel_type = ?,
                    number_of_wheels = ?,
                    motorcycle_type = ?,
                    cargo_capacity = ?,
                    transmission_type = ?,
                    available = ?
                WHERE vehicle_id = ?
                """,
                (
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                    data[5],
                    data[6],
                    data[7],
                    data[8],
                    data[9],
                    data[10],
                    data[11],
                    data[0]
                )
            )

            connection.commit()

            if cursor.rowcount == 0:
                raise RepositoryError(
                    f"Vehicle ID '{vehicle.get_vehicle_id()}' "
                    "does not exist."
                )

        finally:
            connection.close()

    def delete_vehicle(self, vehicle_id: str) -> bool:
        """Delete a vehicle from the database."""

        connection = self._connect()

        try:
            cursor = connection.execute(
                """
                DELETE FROM vehicles
                WHERE vehicle_id = ?
                """,
                (vehicle_id.strip().upper(),)
            )

            connection.commit()

            return cursor.rowcount > 0

        finally:
            connection.close()

    def clear_all_vehicles(self) -> None:
        """Delete all vehicles from the database."""

        connection = self._connect()

        try:
            connection.execute(
                """
                DELETE FROM vehicles
                """
            )

            connection.commit()

        finally:
            connection.close()

    def get_vehicle_by_id(self, vehicle_id: str):
        """Retrieve one vehicle by ID."""

        connection = self._connect()

        try:
            cursor = connection.execute(
                """
                SELECT
                    vehicle_id,
                    vehicle_type,
                    make,
                    model,
                    year,
                    number_of_doors,
                    fuel_type,
                    number_of_wheels,
                    motorcycle_type,
                    cargo_capacity,
                    transmission_type,
                    available
                FROM vehicles
                WHERE vehicle_id = ?
                """,
                (vehicle_id.strip().upper(),)
            )

            row = cursor.fetchone()

        finally:
            connection.close()

        if row is None:
            return None

        return self._record_to_vehicle(row)

    def get_all_vehicles(self) -> list:
        """Retrieve all vehicles from the database."""

        connection = self._connect()

        try:
            cursor = connection.execute(
                """
                SELECT
                    vehicle_id,
                    vehicle_type,
                    make,
                    model,
                    year,
                    number_of_doors,
                    fuel_type,
                    number_of_wheels,
                    motorcycle_type,
                    cargo_capacity,
                    transmission_type,
                    available
                FROM vehicles
                ORDER BY vehicle_id
                """
            )

            rows = cursor.fetchall()

        finally:
            connection.close()

        return [
            self._record_to_vehicle(row)
            for row in rows
        ]

    @staticmethod
    def _vehicle_to_record(vehicle) -> tuple:
        """Convert a vehicle object into a database record."""

        vehicle_type = vehicle.__class__.__name__.lower()

        number_of_doors = None
        fuel_type = None
        number_of_wheels = None
        motorcycle_type = None
        cargo_capacity = None
        transmission_type = None

        if isinstance(vehicle, Car):
            number_of_doors = vehicle.get_number_of_doors()
            fuel_type = vehicle.get_fuel_type()

        elif isinstance(vehicle, Motorcycle):
            number_of_wheels = vehicle.get_number_of_wheels()
            motorcycle_type = vehicle.get_motorcycle_type()

        elif isinstance(vehicle, Truck):
            cargo_capacity = vehicle.get_cargo_capacity()
            transmission_type = vehicle.get_transmission_type()

        else:
            raise TypeError(
                "Unsupported vehicle type."
            )

        return (
            vehicle.get_vehicle_id(),
            vehicle_type,
            vehicle.get_make(),
            vehicle.get_model(),
            vehicle.get_year(),
            number_of_doors,
            fuel_type,
            number_of_wheels,
            motorcycle_type,
            cargo_capacity,
            transmission_type,
            1 if vehicle.is_available() else 0
        )

    @staticmethod
    def _record_to_vehicle(row):
        """Convert a database record into a vehicle object."""

        (
            vehicle_id,
            vehicle_type,
            make,
            model,
            year,
            number_of_doors,
            fuel_type,
            number_of_wheels,
            motorcycle_type,
            cargo_capacity,
            transmission_type,
            available
        ) = row

        if vehicle_type == "car":

            vehicle = Car(
                vehicle_id,
                make,
                model,
                year,
                number_of_doors,
                fuel_type
            )

        elif vehicle_type == "motorcycle":

            vehicle = Motorcycle(
                vehicle_id,
                make,
                model,
                year,
                number_of_wheels,
                motorcycle_type
            )

        elif vehicle_type == "truck":

            vehicle = Truck(
                vehicle_id,
                make,
                model,
                year,
                cargo_capacity,
                transmission_type
            )

        else:
            raise ValueError(
                f"Unknown vehicle type: {vehicle_type}"
            )

        vehicle.set_availability(bool(available))

        return vehicle