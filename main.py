import mysql.connector

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="employee_db"
)

cursor = db.cursor()

# Create employee table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    department VARCHAR(100),
    salary FLOAT
)
""")

# Add employee
def add_employee():
    name = input("Enter employee name: ")
    email = input("Enter email: ")
    department = input("Enter department: ")
    salary = float(input("Enter salary: "))

    query = """
    INSERT INTO employees (name, email, department, salary)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (name, email, department, salary))
    db.commit()
    print("Employee added successfully!")

# View employees
def view_employees():
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()

    for employee in records:
        print(employee)

# Update employee
def update_employee():
    emp_id = int(input("Enter employee ID: "))
    salary = float(input("Enter new salary: "))

    cursor.execute(
        "UPDATE employees SET salary=%s WHERE id=%s",
        (salary, emp_id)
    )
    db.commit()
    print("Employee updated successfully!")

# Delete employee
def delete_employee():
    emp_id = int(input("Enter employee ID: "))

    cursor.execute(
        "DELETE FROM employees WHERE id=%s",
        (emp_id,)
    )
    db.commit()
    print("Employee deleted successfully!")

# Search employee
def search_employee():
    emp_id = int(input("Enter employee ID: "))

    cursor.execute(
        "SELECT * FROM employees WHERE id=%s",
        (emp_id,)
    )
    print(cursor.fetchall())

# Main menu
while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee Salary")
    print("4. Delete Employee")
    print("5. Search Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        view_employees()
    elif choice == "3":
        update_employee()
    elif choice == "4":
        delete_employee()
    elif choice == "5":
        search_employee()
    elif choice == "6":
        break
    else:
        print("Invalid choice!")

cursor.close()
db.close()
