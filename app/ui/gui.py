import tkinter as tk
from tkinter import ttk, messagebox


class VehicleGUI:
    """Professional Tkinter GUI for the Vehicle Information System."""

    def __init__(self, service):
        self.service = service

        self.root = tk.Tk()
        self.root.title("Exodus Cars - Vehicle Rental Management System")
        self.root.geometry("1250x750")
        self.root.minsize(1050, 650)

        self.search_var = tk.StringVar()
        self.filter_var = tk.StringVar(value="All Vehicles")

        self._configure_style()
        self._build_interface()
        self.refresh_vehicle_table()

    # ============================================================
    # STYLE
    # ============================================================

    def _configure_style(self):
        """Configure application styling."""

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure(
            "Title.TLabel",
            font=("Segoe UI", 24, "bold")
        )

        style.configure(
            "Subtitle.TLabel",
            font=("Segoe UI", 10)
        )

        style.configure(
            "Card.TFrame",
            relief="solid",
            borderwidth=1
        )

        style.configure(
            "CardTitle.TLabel",
            font=("Segoe UI", 10)
        )

        style.configure(
            "CardValue.TLabel",
            font=("Segoe UI", 20, "bold")
        )

        style.configure(
            "Treeview",
            font=("Segoe UI", 10),
            rowheight=30
        )

        style.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

        style.configure(
            "Action.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(12, 8)
        )

        style.configure(
            "Danger.TButton",
            font=("Segoe UI", 10, "bold"),
            padding=(12, 8)
        )

    # ============================================================
    # MAIN INTERFACE
    # ============================================================

    def _build_interface(self):
        """Build the complete application interface."""

        # --------------------------------------------------------
        # Header
        # --------------------------------------------------------

        header = ttk.Frame(self.root, padding=(20, 18))
        header.pack(fill="x")

        ttk.Label(
            header,
            text="EXODUS CARS",
            style="Title.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            header,
            text="Vehicle Rental Management System",
            style="Subtitle.TLabel"
        ).pack(anchor="w")

        # --------------------------------------------------------
        # Statistics
        # --------------------------------------------------------

        stats_frame = ttk.Frame(self.root, padding=(20, 5))
        stats_frame.pack(fill="x")

        self.total_value = self._create_stat_card(
            stats_frame,
            "TOTAL VEHICLES"
        )

        self.cars_value = self._create_stat_card(
            stats_frame,
            "CARS"
        )

        self.motorcycles_value = self._create_stat_card(
            stats_frame,
            "MOTORCYCLES"
        )

        self.trucks_value = self._create_stat_card(
            stats_frame,
            "TRUCKS"
        )

        self.available_value = self._create_stat_card(
            stats_frame,
            "AVAILABLE"
        )

        self.rented_value = self._create_stat_card(
            stats_frame,
            "RENTED"
        )

        # --------------------------------------------------------
        # Toolbar
        # --------------------------------------------------------

        toolbar = ttk.Frame(self.root, padding=(20, 15))
        toolbar.pack(fill="x")

        ttk.Label(
            toolbar,
            text="Search:"
        ).pack(side="left")

        search_entry = ttk.Entry(
            toolbar,
            textvariable=self.search_var,
            width=35
        )

        search_entry.pack(
            side="left",
            padx=(8, 15)
        )

        search_entry.bind(
            "<KeyRelease>",
            lambda event: self.refresh_vehicle_table()
        )

        ttk.Label(
            toolbar,
            text="Filter:"
        ).pack(side="left")

        filter_box = ttk.Combobox(
            toolbar,
            textvariable=self.filter_var,
            values=[
                "All Vehicles",
                "Available",
                "Rented"
            ],
            state="readonly",
            width=15
        )

        filter_box.pack(
            side="left",
            padx=(8, 15)
        )

        filter_box.bind(
            "<<ComboboxSelected>>",
            lambda event: self.refresh_vehicle_table()
        )

        ttk.Button(
            toolbar,
            text="Clear Search",
            command=self.clear_search
        ).pack(side="left")

        # --------------------------------------------------------
        # Vehicle Actions
        # --------------------------------------------------------

        action_frame = ttk.Frame(
            self.root,
            padding=(20, 5)
        )

        action_frame.pack(fill="x")

        ttk.Button(
            action_frame,
            text="+ Add Vehicle",
            style="Action.TButton",
            command=self.open_add_vehicle_dialog
        ).pack(side="left", padx=(0, 8))

        ttk.Button(
            action_frame,
            text="Edit Vehicle",
            style="Action.TButton",
            command=self.edit_selected_vehicle
        ).pack(side="left", padx=8)

        ttk.Button(
            action_frame,
            text="Delete Vehicle",
            style="Danger.TButton",
            command=self.delete_selected_vehicle
        ).pack(side="left", padx=8)

        ttk.Button(
            action_frame,
            text="Rent Selected",
            command=self.rent_selected_vehicle
        ).pack(side="left", padx=5)

        ttk.Button(
            action_frame,
            text="Return Selected",
            command=self.return_selected_vehicle
        ).pack(side="left", padx=5)

        # --------------------------------------------------------
        # Table
        # --------------------------------------------------------

        table_frame = ttk.Frame(
            self.root,
            padding=(20, 10)
        )

        table_frame.pack(
            fill="both",
            expand=True
        )

        columns = (
            "id",
            "type",
            "make",
            "model",
            "year",
            "details",
            "status"
        )

        # Professional vehicle table styling
        style = ttk.Style()

        style.configure(
            "Treeview",
            background="white",
            foreground="#243B53",
            rowheight=32,
            fieldbackground="white",
            font=("Segoe UI", 10)
        )

        style.configure(
    "Treeview.Heading",
    background="#243B53",
    foreground="white",
    font=("Segoe UI", 10, "bold"),
    padding=8
)

        style.map(
            "Treeview",
            background=[("selected", "#D9EAF7")],
            foreground=[("selected", "#102A43")]
        )

        self.vehicle_table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            selectmode="browse"
        )

        self.vehicle_table.heading(
            "id",
            text="Vehicle ID"
        )

        self.vehicle_table.heading(
            "type",
            text="Type"
        )

        self.vehicle_table.heading(
            "make",
            text="Make"
        )

        self.vehicle_table.heading(
            "model",
            text="Model"
        )

        self.vehicle_table.heading(
            "year",
            text="Year"
        )

        self.vehicle_table.heading(
            "details",
            text="Details"
        )

        self.vehicle_table.heading(
            "status",
            text="Status"
        )
        self.vehicle_table.column("id", width=100, anchor="center")
        self.vehicle_table.column("type", width=110, anchor="center")
        self.vehicle_table.column("make", width=120, anchor="w")
        self.vehicle_table.column("model", width=140, anchor="w")
        self.vehicle_table.column("year", width=70, anchor="center")
        self.vehicle_table.column("details", width=220, anchor="w")
        self.vehicle_table.column("status", width=100, anchor="center")
        self.vehicle_table.column(
            "id",
            width=120,
            anchor="center"
        )

        self.vehicle_table.column(
            "type",
            width=110,
            anchor="center"
        )

        self.vehicle_table.column(
            "make",
            width=140
        )

        self.vehicle_table.column(
            "model",
            width=150
        )

        self.vehicle_table.column(
            "year",
            width=80,
            anchor="center"
        )

        self.vehicle_table.column(
            "details",
            width=220
        )

        self.vehicle_table.column(
            "status",
            width=120,
            anchor="center"
        )

        # Scrollbars

        vertical_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.vehicle_table.yview
        )

        horizontal_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=self.vehicle_table.xview
        )

        self.vehicle_table.configure(
            yscrollcommand=vertical_scrollbar.set,
            xscrollcommand=horizontal_scrollbar.set
        )

        self.vehicle_table.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        vertical_scrollbar.grid(
            row=0,
            column=1,
            sticky="ns"
        )

        horizontal_scrollbar.grid(
            row=1,
            column=0,
            sticky="ew"
        )

        table_frame.rowconfigure(
            0,
            weight=1
        )

        table_frame.columnconfigure(
            0,
            weight=1
        )

        # Double click to edit

        self.vehicle_table.bind(
            "<Double-1>",
            lambda event: self.edit_selected_vehicle()
        )

        # --------------------------------------------------------
        # Bottom controls
        # --------------------------------------------------------

        bottom = ttk.Frame(
            self.root,
            padding=(20, 10)
        )

        bottom.pack(fill="x")

        ttk.Button(
            bottom,
            text="Rent Selected",
            style="Action.TButton",
            command=self.rent_selected_vehicle
        ).pack(side="left", padx=(0, 8))

        ttk.Button(
            bottom,
            text="Return Selected",
            style="Action.TButton",
            command=self.return_selected_vehicle
        ).pack(side="left", padx=8)

        ttk.Button(
            bottom,
            text="Refresh",
            command=self.refresh_vehicle_table
        ).pack(side="left", padx=8)

        ttk.Button(
            bottom,
            text="Exit",
            command=self.confirm_exit
        ).pack(side="right")

    # ============================================================
    # STATISTICS
    # ============================================================
   
    def _create_stat_card(self, parent, title):
            """Create a dashboard statistics card."""
            card = tk.Frame(
        parent,
            bg="white",
            highlightbackground="#D9E2EC",
            highlightthickness=1,
            bd=0
        )

            card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=6,
            pady=8,
            ipady=8
        )

            # Colored accent at the top of the card
            accent_colors = {
                "TOTAL VEHICLES": "#243B53",
                "CARS": "#2563EB",
                "MOTORCYCLES": "#7C3AED",
                "TRUCKS": "#D97706",
                "AVAILABLE": "#15803D",
                "RENTED": "#DC2626"
            }

            accent_color = accent_colors.get(title.upper(), "#243B53")

            tk.Frame(
                card,
                bg=accent_color,
                height=5
            ).pack(fill="x")

            # Card title
            tk.Label(
                card,
                text=title,
                bg="white",
                fg="#526579",
                font=("Segoe UI", 9, "bold")
            ).pack(pady=(12, 5))

            # Value displayed in the card
            value_label = tk.Label(
                card,
                text="0",
                bg="white",
                fg="#102A43",
                font=("Segoe UI", 24, "bold")
            )
            value_label.pack(pady=(0, 12))

            return value_label


    def update_statistics(self):
        """Update dashboard statistics."""

        stats = self.service.get_vehicle_statistics()

        self.total_value.config(
            text=str(stats.get("total", 0))
        )

        self.cars_value.config(
            text=str(stats.get("cars", 0))
        )

        self.motorcycles_value.config(
            text=str(stats.get("motorcycles", 0))
        )

        self.trucks_value.config(
            text=str(stats.get("trucks", 0))
        )

        self.available_value.config(
            text=str(stats.get("available", 0))
        )

        self.rented_value.config(
            text=str(stats.get("rented", 0))
        )

    # ============================================================
    # TABLE
    # ============================================================

    def refresh_vehicle_table(self):
        """Refresh vehicle table according to search and filter."""

        for item in self.vehicle_table.get_children():
            self.vehicle_table.delete(item)

        vehicles = self.service.get_all_vehicles()

        search_text = self.search_var.get().strip().lower()
        selected_filter = self.filter_var.get()

        for vehicle in vehicles:

            vehicle_id = vehicle.get_vehicle_id()
            make = vehicle.get_make()
            model = vehicle.get_model()
            year = vehicle.get_year()

            vehicle_type = type(vehicle).__name__

            # ----------------------------------------------------
            # Search
            # ----------------------------------------------------

            searchable_text = (
                f"{vehicle_id} "
                f"{vehicle_type} "
                f"{make} "
                f"{model} "
                f"{year}"
            ).lower()

            if search_text and search_text not in searchable_text:
                continue

            # ----------------------------------------------------
            # Filter
            # ----------------------------------------------------

            if (
                selected_filter == "Available"
                and not vehicle.is_available()
            ):
                continue

            if (
                selected_filter == "Rented"
                and vehicle.is_available()
            ):
                continue

            # ----------------------------------------------------
            # Determine details
            # ----------------------------------------------------

            details = self._get_vehicle_details(vehicle)

            status = "Available" if vehicle.is_available() else "Rented"
            tag = "available" if vehicle.is_available() else "rented"

            self.vehicle_table.insert(
                "",
                "end",
                values=(
                    vehicle_id,
                    vehicle_type,
                    make,
                    model,
                    year,
                    details,
                    status
                ),
                tags=(tag,)
            )

            self.vehicle_table.tag_configure(
                "available",
                foreground="#198754"
)

            self.vehicle_table.tag_configure(
                "rented",
                 foreground="#DC3545"
)
            self.update_statistics()

    def _get_vehicle_details(self, vehicle):
        """Return vehicle-specific information."""

        vehicle_type = type(vehicle).__name__

        if vehicle_type == "Car":
            return (
                f"Doors: {vehicle.get_number_of_doors()} | "
                f"Fuel: {vehicle.get_fuel_type()}"
            )

        if vehicle_type == "Motorcycle":
            return (
                f"Wheels: {vehicle.get_number_of_wheels()} | "
                f"Type: {vehicle.get_motorcycle_type()}"
            )

        if vehicle_type == "Truck":
            return (
                f"Cargo: {vehicle.get_cargo_capacity()} | "
                f"Transmission: {vehicle.get_transmission_type()}"
            )

        return ""

    # ============================================================
    # SEARCH
    # ============================================================

    def clear_search(self):
        """Clear search field."""

        self.search_var.set("")
        self.filter_var.set("All Vehicles")
        self.refresh_vehicle_table()

    # ============================================================
    # SELECTED VEHICLE
    # ============================================================

    def _get_selected_vehicle_id(self):
        """Return selected vehicle ID."""

        selection = self.vehicle_table.selection()

        if not selection:
            messagebox.showwarning(
                "No Selection",
                "Please select a vehicle first."
            )
            return None

        values = self.vehicle_table.item(
            selection[0],
            "values"
        )

        if not values:
            return None

        return values[0]

    # ============================================================
    # ADD VEHICLE
    # ============================================================

    def open_add_vehicle_dialog(self):
        """Open Add Vehicle dialog."""

        dialog = tk.Toplevel(self.root)
        dialog.title("Add Vehicle")
        dialog.geometry("480x500")
        dialog.resizable(False, False)

        container = ttk.Frame(
            dialog,
            padding=25
        )

        container.pack(
            fill="both",
            expand=True
        )

        ttk.Label(
            container,
            text="Add New Vehicle",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w", pady=(0, 20))

        form = ttk.Frame(container)
        form.pack(fill="x")

        # Variables

        vehicle_type = tk.StringVar(value="Car")
        vehicle_id = tk.StringVar()
        make = tk.StringVar()
        model = tk.StringVar()
        year = tk.StringVar()

        extra_label_1 = tk.StringVar()
        extra_value_1 = tk.StringVar()

        extra_label_2 = tk.StringVar()
        extra_value_2 = tk.StringVar()

        # Vehicle Type

        ttk.Label(
            form,
            text="Vehicle Type"
        ).grid(row=0, column=0, sticky="w", pady=6)

        type_box = ttk.Combobox(
            form,
            textvariable=vehicle_type,
            values=[
                "Car",
                "Motorcycle",
                "Truck"
            ],
            state="readonly"
        )

        type_box.grid(
            row=0,
            column=1,
            sticky="ew",
            pady=6
        )

        # Standard fields

        fields = [
            ("Vehicle ID", vehicle_id),
            ("Make", make),
            ("Model", model),
            ("Year", year)
        ]

        for row, (label, variable) in enumerate(
            fields,
            start=1
        ):
            ttk.Label(
                form,
                text=label
            ).grid(
                row=row,
                column=0,
                sticky="w",
                pady=6
            )

            ttk.Entry(
                form,
                textvariable=variable
            ).grid(
                row=row,
                column=1,
                sticky="ew",
                pady=6
            )

        # Dynamic fields

        ttk.Label(
            form,
            textvariable=extra_label_1
        ).grid(
            row=5,
            column=0,
            sticky="w",
            pady=6
        )

        extra_entry_1 = ttk.Entry(
            form,
            textvariable=extra_value_1
        )

        extra_entry_1.grid(
            row=5,
            column=1,
            sticky="ew",
            pady=6
        )

        ttk.Label(
            form,
            textvariable=extra_label_2
        ).grid(
            row=6,
            column=0,
            sticky="w",
            pady=6
        )

        extra_entry_2 = ttk.Entry(
            form,
            textvariable=extra_value_2
        )

        extra_entry_2.grid(
            row=6,
            column=1,
            sticky="ew",
            pady=6
        )

        form.columnconfigure(
            1,
            weight=1
        )

        def update_dynamic_fields(*args):
            """Update fields based on vehicle type."""

            selected = vehicle_type.get()

            if selected == "Car":
                extra_label_1.set("Number of Doors")
                extra_label_2.set("Fuel Type")

            elif selected == "Motorcycle":
                extra_label_1.set("Number of Wheels")
                extra_label_2.set("Motorcycle Type")

            elif selected == "Truck":
                extra_label_1.set("Cargo Capacity")
                extra_label_2.set("Transmission")

        vehicle_type.trace_add(
            "write",
            update_dynamic_fields
        )

        update_dynamic_fields()

        # Buttons

        buttons = ttk.Frame(container)
        buttons.pack(
            fill="x",
            pady=(25, 0)
        )

        def save_vehicle():
            try:
                from app.models.car import Car
                from app.models.motorcycle import Motorcycle
                from app.models.truck import Truck

                selected = vehicle_type.get()

                vid = vehicle_id.get().strip()
                vehicle_make = make.get().strip()
                vehicle_model = model.get().strip()
                vehicle_year = int(year.get())

                value_1 = extra_value_1.get().strip()
                value_2 = extra_value_2.get().strip()

                if selected == "Car":

                    vehicle = Car(
                        vid,
                        vehicle_make,
                        vehicle_model,
                        vehicle_year,
                        int(value_1),
                        value_2
                    )

                elif selected == "Motorcycle":

                    vehicle = Motorcycle(
                        vid,
                        vehicle_make,
                        vehicle_model,
                        vehicle_year,
                        int(value_1),
                        value_2
                    )

                else:

                    vehicle = Truck(
                        vid,
                        vehicle_make,
                        vehicle_model,
                        vehicle_year,
                        float(value_1),
                        value_2
                    )

                self.service.add_vehicle(vehicle)

                messagebox.showinfo(
                    "Success",
                    f"{selected} {vid.upper()} was added successfully."
                )

                dialog.destroy()
                self.refresh_vehicle_table()

            except ValueError as error:

                messagebox.showerror(
                    "Invalid Input",
                    str(error)
                )

            except Exception as error:

                messagebox.showerror(
                    "Unable to Add Vehicle",
                    str(error)
                )

        ttk.Button(
            buttons,
            text="Cancel",
            command=dialog.destroy
        ).pack(side="right", padx=5)

        ttk.Button(
            buttons,
            text="Save Vehicle",
            style="Action.TButton",
            command=save_vehicle
        ).pack(side="right", padx=5)

    # ============================================================
    # EDIT VEHICLE
    # ============================================================

    def edit_selected_vehicle(self):
        """Edit the selected vehicle."""

        vehicle_id = self._get_selected_vehicle_id()

        if vehicle_id is None:
            return

        vehicle = self.service.find_vehicle_by_id(vehicle_id)

        if vehicle is None:
            messagebox.showerror(
                "Error",
                "Vehicle could not be found."
            )
            return

        dialog = tk.Toplevel(self.root)
        dialog.title("Edit Vehicle")
        dialog.geometry("450x350")
        dialog.resizable(False, False)

        container = ttk.Frame(
            dialog,
            padding=25
        )

        container.pack(
            fill="both",
            expand=True
        )

        ttk.Label(
            container,
            text="Edit Vehicle",
            font=("Segoe UI", 18, "bold")
        ).pack(anchor="w", pady=(0, 20))

        form = ttk.Frame(container)
        form.pack(fill="x")

        make_var = tk.StringVar(
            value=vehicle.get_make()
        )

        model_var = tk.StringVar(
            value=vehicle.get_model()
        )

        year_var = tk.StringVar(
            value=str(vehicle.get_year())
        )

        fields = [
            ("Vehicle ID", vehicle.get_vehicle_id()),
            ("Make", make_var),
            ("Model", model_var),
            ("Year", year_var)
        ]

        for row, (label, value) in enumerate(fields):

            ttk.Label(
                form,
                text=label
            ).grid(
                row=row,
                column=0,
                sticky="w",
                pady=8
            )

            if isinstance(value, tk.StringVar):

                ttk.Entry(
                    form,
                    textvariable=value
                ).grid(
                    row=row,
                    column=1,
                    sticky="ew",
                    pady=8
                )

            else:

                ttk.Label(
                    form,
                    text=value
                ).grid(
                    row=row,
                    column=1,
                    sticky="w",
                    pady=8
                )

        form.columnconfigure(
            1,
            weight=1
        )

        def save_changes():

            try:

                updates = {
                    "make": make_var.get().strip(),
                    "model": model_var.get().strip(),
                    "year": int(year_var.get())
                }

                self.service.update_vehicle(
                    vehicle_id,
                    **updates
                )

                messagebox.showinfo(
                    "Success",
                    "Vehicle updated successfully."
                )

                dialog.destroy()
                self.refresh_vehicle_table()

            except Exception as error:

                messagebox.showerror(
                    "Update Failed",
                    str(error)
                )

        buttons = ttk.Frame(container)
        buttons.pack(
            fill="x",
            pady=(25, 0)
        )

        ttk.Button(
            buttons,
            text="Cancel",
            command=dialog.destroy
        ).pack(
            side="right",
            padx=5
        )

        ttk.Button(
            buttons,
            text="Save Changes",
            style="Action.TButton",
            command=save_changes
        ).pack(
            side="right",
            padx=5
        )

    # ============================================================
    # DELETE
    # ============================================================

    def delete_selected_vehicle(self):
        """Delete selected vehicle."""

        vehicle_id = self._get_selected_vehicle_id()

        if vehicle_id is None:
            return

        confirmed = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete {vehicle_id}?"
        )

        if not confirmed:
            return

        try:

            self.service.remove_vehicle(vehicle_id)

            messagebox.showinfo(
                "Vehicle Deleted",
                f"{vehicle_id} was deleted successfully."
            )

            self.refresh_vehicle_table()

        except Exception as error:

            messagebox.showerror(
                "Delete Failed",
                str(error)
            )

    # ============================================================
    # RENT
    # ============================================================

    def rent_selected_vehicle(self):
        """Rent selected vehicle."""

        vehicle_id = self._get_selected_vehicle_id()

        if vehicle_id is None:
            return

        vehicle = self.service.find_vehicle_by_id(
            vehicle_id
        )

        if vehicle is None:
            messagebox.showerror(
                "Error",
                "Vehicle not found."
            )
            return

        if not vehicle.is_available():
            messagebox.showwarning(
                "Vehicle Unavailable",
                f"{vehicle_id} is already rented."
            )
            return

        confirmed = messagebox.askyesno(
            "Confirm Rental",
            f"Rent vehicle {vehicle_id}?"
        )

        if not confirmed:
            return

        try:

            self.service.rent_vehicle(
                vehicle_id
            )

            messagebox.showinfo(
                "Rental Successful",
                f"{vehicle_id} has been rented."
            )

            self.refresh_vehicle_table()

        except Exception as error:

            messagebox.showerror(
                "Rental Failed",
                str(error)
            )

    # ============================================================
    # RETURN
    # ============================================================

    def return_selected_vehicle(self):
        """Return selected vehicle."""

        vehicle_id = self._get_selected_vehicle_id()

        if vehicle_id is None:
            return

        vehicle = self.service.find_vehicle_by_id(
            vehicle_id
        )

        if vehicle is None:
            messagebox.showerror(
                "Error",
                "Vehicle not found."
            )
            return

        if vehicle.is_available():
            messagebox.showwarning(
                "Vehicle Available",
                f"{vehicle_id} is not currently rented."
            )
            return

        confirmed = messagebox.askyesno(
            "Confirm Return",
            f"Return vehicle {vehicle_id}?"
        )

        if not confirmed:
            return

        try:

            self.service.return_vehicle(
                vehicle_id
            )

            messagebox.showinfo(
                "Return Successful",
                f"{vehicle_id} has been returned."
            )

            self.refresh_vehicle_table()

        except Exception as error:

            messagebox.showerror(
                "Return Failed",
                str(error)
            )

    # ============================================================
    # EXIT
    # ============================================================

    def confirm_exit(self):
        """Confirm application exit."""

        confirmed = messagebox.askyesno(
            "Exit Application",
            "Are you sure you want to exit?"
        )

        if confirmed:
            self.root.destroy()

    # ============================================================
    # RUN
    # ============================================================

    def run(self):
        """Start the GUI."""

        self.root.mainloop()