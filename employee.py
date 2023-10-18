import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mahi@777",
    database="employee_management"
)

# Create a cursor to execute SQL queries
cursor = db.cursor()

# Function to add an employee
def add_employee(first_name, last_name, department, salary):
    sql = "INSERT INTO employees (first_name, last_name, department, salary) VALUES (%s, %s, %s, %s)"
    values = (first_name, last_name, department, salary)

    cursor.execute(sql, values)
    db.commit()
    print("Employee added successfully!")

# Function to view all employees
def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    for employee in employees:
        print(employee)

# Function to update an employee
def update_employee(employee_id, first_name, last_name, department, salary):
    sql = "UPDATE employees SET first_name = %s, last_name = %s, department = %s, salary = %s WHERE employee_id = %s"
    values = (first_name, last_name, department, salary, employee_id)

    cursor.execute(sql, values)
    db.commit()
    print("Employee information updated successfully!")

# Function to delete an employee
def delete_employee(employee_id):
    sql = "DELETE FROM employees WHERE employee_id = %s"
    values = (employee_id,)

    cursor.execute(sql, values)
    db.commit()
    print("Employee deleted successfully!")

# Main menu
while True:
    print("\nEmployee Information System")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))
        add_employee(first_name, last_name, department, salary)
    elif choice == "2":
        view_employees()
    elif choice == "3":
        employee_id = int(input("Enter the ID of the employee to update: "))
        first_name = input("Enter updated first name: ")
        last_name = input("Enter updated last name: ")
        department = input("Enter updated department: ")
        salary = float(input("Enter updated salary: "))
        update_employee(employee_id, first_name, last_name, department, salary)
    elif choice == "4":
        employee_id = int(input("Enter the ID of the employee to delete: "))
        delete_employee(employee_id)
    elif choice == "5":
        break

# Close the database connection
db.close()

