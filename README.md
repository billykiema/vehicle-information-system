# Vehicle Information System

A Python-based vehicle rental management application built with object-oriented programming, Tkinter, SQLite, and pytest. The system provides a graphical interface for managing cars, motorcycles, and trucks, monitoring vehicle availability, and recording rental and return operations.

## Project Overview

The Vehicle Information System was developed to demonstrate practical Python programming skills, object-oriented design, database integration, GUI development, and automated testing.

The application allows users to manage vehicle records through a desktop interface while maintaining vehicle information and rental status in a local SQLite database.

## Features

- **Vehicle management:** Add, view, edit, and delete vehicle records.
- **Multiple vehicle types:** Manage cars, motorcycles, and trucks.
- **Rental management:** Rent available vehicles and return rented vehicles.
- **Dashboard:** View vehicle totals, vehicle categories, availability, and rental status.
- **Search and filtering:** Find vehicles and narrow displayed results.
- **Data persistence:** Store vehicle information in an SQLite database.
- **Input validation:** Validate vehicle information before processing operations.
- **Error handling:** Handle invalid inputs and common application errors.
- **Graphical user interface:** Use a Tkinter desktop interface to interact with the system.
- **Automated testing:** Use pytest to test application functionality.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Object-oriented programming (OOP) | Organizing vehicle types and application logic |
| Abstract base classes (ABC) | Defining common vehicle behavior |
| Tkinter | Desktop graphical user interface |
| SQLite | Local database storage |
| pytest | Automated testing |
| Git and GitHub | Version control and project hosting |
| Visual Studio Code | Development environment |

## Application Screenshots

Screenshots of the running application can be added to the `screenshots/` folder.

To display a screenshot on the GitHub README, save an image in that folder and add a Markdown image reference. For example:

```markdown
![Vehicle Information System dashboard](screenshots/dashboard.png)
```

Replace `dashboard.png` with the actual screenshot filename.

## Project Structure

The project is organized into separate modules to improve maintainability and separation of concerns.

```text
VehicleInformationSystem/
├── app/
│   ├── interfaces/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   └── ui/
│       ├── console_ui.py
│       └── gui.py
├── database/
│   └── vehicle_rental.db
├── tests/
├── screenshots/
├── main.py
├── gui_main.py
├── requirements.txt
├── .gitignore
└── README.md
```

*Note: This is a summary of the expected project layout. Adjust the tree to match the actual files and folders in your repository.*

## Requirements

- Python 3.10 or later is recommended, subject to compatibility with your project and installed dependencies.
- pip, Python's package installer.
- Git, if you intend to clone the repository.
- Visual Studio Code or another Python-compatible editor is optional.

## Installation and Setup

### 1. Clone the repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/vehicle-information-system.git
cd vehicle-information-system
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, you can use the appropriate Python executable inside `.venv` without activating the environment.

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Running the Application

To launch the graphical interface, run:

```powershell
python gui_main.py
```

If you want to use the console interface, check the entry point in `main.py` and run it if it launches that interface:

```powershell
python main.py
```

## Running the Tests

Run the automated test suite from the project root:

```powershell
python -m pytest
```

To display more detailed test results:

```powershell
python -m pytest -v
```

The test suite has previously passed **68 tests** during development. Run the commands above to verify the current version after making changes.

## Design and Architecture

The application separates responsibilities into different parts:

- **Interfaces:** Define common vehicle behavior and shared contracts.
- **Models:** Represent vehicle types and their attributes.
- **Repositories:** Handle database-related operations.
- **Services:** Manage application operations and business rules.
- **User interfaces:** Provide graphical and console-based interaction.
- **Tests:** Check that application components behave as expected.

This organization makes the application easier to understand, test, and extend than a single large Python file.

## Future Improvements

Potential enhancements include:

- User authentication and role-based permissions.
- Rental pricing and invoice generation.
- Rental history and reporting.
- Improved input validation and user feedback.
- Database backup and restoration.
- Automated continuous integration with GitHub Actions.
- Additional unit and integration tests.

## Learning Outcomes

This project demonstrates practical experience with:

- Python classes, inheritance, and abstraction.
- Modular application development.
- GUI programming with Tkinter.
- SQLite database integration.
- Automated testing with pytest.
- Version control using Git and GitHub.
- Organizing a software project for maintainability.

## Author

Developed as a programming and portfolio project to practise software development principles and build practical experience with Python.

## License

No license has been specified yet. If you intend to make the project open source, consider choosing a license and adding a corresponding `LICENSE` file.
