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