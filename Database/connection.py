import pyodbc


def get_connection():

    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=.;"
        "DATABASE=EmployeeManagementDB;"
        "Trusted_Connection=yes;"
        "TrustServerCertificate=yes;"
    )

    return connection