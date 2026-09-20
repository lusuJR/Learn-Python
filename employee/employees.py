from Database.connection import get_connection


def add_employee(name, department, salary):

    # Connect to SQL Server
    connection = get_connection()

    # Create a cursor
    cursor = connection.cursor()

    # SQL INSERT statement
    sql = """
        INSERT INTO Employees
        (FullName, Department, Salary)
        VALUES (?, ?, ?)
    """

    # Execute SQL
    cursor.execute(
        sql,
        name,
        department,
        salary
    )

    # Save changes
    connection.commit()

    # Close connection
    cursor.close()
    connection.close()

    print("Employee added successfully!")

#Get all employees

def get_all_employees():

    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        SELECT EmployeeID,
               FullName,
               Department,
               Salary
        FROM Employees
    """

    cursor.execute(sql)

    employees = cursor.fetchall()

    cursor.close()
    connection.close()

    return employees
  