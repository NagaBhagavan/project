# Employee Management System

This project provides a simple Employee Management System that connects to an SQL Server database using Python. It allows for the management of employee records including adding, updating, and deleting employees, as well as querying the database for specific employee data.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Connect to an SQL Server database
- Add new employee records
- Update existing employee records
- Delete employee records
- Query employee data

## Requirements

- Python 3.x
- SQL Server
- Required Python libraries (listed in `requirements.txt`)

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/employee-management-system.git
    cd employee-management-system
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python -m venv venv
    source venv/bin/activate    # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required Python libraries**:
    ```sh
    pip install -r requirements.txt
    ```

## Configuration

1. **Set up your SQL Server database**:
    - Ensure SQL Server is installed and running.
    - Create a database named `EmployeeDB`.
    - Create a table named `Employees` with the following schema:
        ```sql
        CREATE TABLE Employees (
            EmployeeID INT PRIMARY KEY IDENTITY(1,1),
            FirstName NVARCHAR(50),
            LastName NVARCHAR(50),
            Email NVARCHAR(50),
            Phone NVARCHAR(20),
            HireDate DATE,
            JobTitle NVARCHAR(50)
        );
        ```

2. **Update database connection settings**:
    - Edit the `config.py` file to include your SQL Server connection details:
        ```python
        config = {
            'server': 'your_server_name',
            'database': 'EmployeeDB',
            'username': 'your_username',
            'password': 'your_password',
        }
        ```

## Usage

1. **Run the main script**:
    ```sh
    python main.py
    ```

2. **Example operations**:
    - Adding a new employee:
        ```python
        from employee_manager import add_employee

        new_employee = {
            'FirstName': 'John',
            'LastName': 'Doe',
            'Email': 'johndoe@example.com',
            'Phone': '123-456-7890',
            'HireDate': '2023-01-01',
            'JobTitle': 'Software Engineer'
        }

        add_employee(new_employee)
        ```

    - Updating an existing employee:
        ```python
        from employee_manager import update_employee

        updated_employee = {
            'EmployeeID': 1,
            'FirstName': 'John',
            'LastName': 'Smith',
            'Email': 'johnsmith@example.com',
            'Phone': '098-765-4321',
            'HireDate': '2023-01-01',
            'JobTitle': 'Senior Software Engineer'
        }

        update_employee(updated_employee)
        ```

    - Deleting an employee:
        ```python
        from employee_manager import delete_employee

        delete_employee(1)
        ```

    - Querying employees:
        ```python
        from employee_manager import get_all_employees, get_employee_by_id

        all_employees = get_all_employees()
        employee = get_employee_by_id(1)
        ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

