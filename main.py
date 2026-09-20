from employee.employees import add_employee


print("====================================")
print("     EMPLOYEE MANAGEMENT SYSTEM")
print("====================================")

name = input("Enter employee full name: ")
department = input("Enter department: ")
salary = float(input("Enter salary: R"))


add_employee(
    name,
    department,
    salary
)