from Database.connection import get_connection


try:
    connection = get_connection()

    print("Connected to SQL Server successfully!")

    connection.close()

except Exception as error:
    print("Database connection failed!")
    print(error)