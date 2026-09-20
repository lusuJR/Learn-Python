from employee.employees import (
    get_all_employees, 
    get_employee_by_id,
    update_employee,
    delete_employee

) 


print("====================================")
print("     EMPLOYEE LIST")
print("====================================")

employees = get_all_employees()

for employee in employees:

    print(f"Employee ID : {employee[0]}")
    print(f"Name : {employee[1]}")
    print(f"Department : {employee[2]}")
    print(f"Salary : R {employee[3]}")

    print("----------------------------")

#Search by ID
print("\n========== SEARCH EMPLOYEE ==========")

employee_id = int(input("Enter Employee ID: "))

employee = get_employee_by_id(employee_id)

if employee:

    print("\nEmployee Found!")
    print(f"Employee ID : {employee[0]}")
    print(f"Name : {employee[1]}")
    print(f"Department : {employee[2]}")
    print(f"Salary : R {employee[3]:.2f}")

else:
    print("Employee not found.")


#Update employee details:
print("\n========== UPDATE EMPLOYEE ==========")

employee_id = int(
    input("Enter Employee ID to update: ")
)

employee = get_employee_by_id(employee_id)

if employee:

    print("\nCurrent Employee Details")
    print(f"Name       : {employee[1]}")
    print(f"Department : {employee[2]}")
    print(f"Salary     : R {employee[3]:.2f}")

    print("\nEnter New Details")

    name = input("Enter new name: ")
    department = input("Enter new department: ")
    salary = float(input("Enter new salary: R"))

    rows_updated = update_employee(
        employee_id,
        name,
        department,
        salary
    )

    if rows_updated > 0:
        print("\nEmployee updated successfully!")

else:
    print("\nEmployee not found.")


#Delete Employee
print("\n========== DELETE EMPLOYEE ==========")

employee_id = int(
    input("Enter Employee ID to delete: ")
)

employee = get_employee_by_id(employee_id)

if employee:

    print("\nEmployee Found")
    print(f"Employee ID : {employee[0]}")
    print(f"Name        : {employee[1]}")
    print(f"Department  : {employee[2]}")
    print(f"Salary      : R {employee[3]:.2f}")

    confirmation = input(
        "\nAre you sure you want to delete this employee? (yes/no): "
    )

    if confirmation.lower() == "yes":

        rows_deleted = delete_employee(employee_id)

        if rows_deleted > 0:
            print("\nEmployee deleted successfully!")

    else:
        print("\nDelete cancelled.")

else:
    print("\nEmployee not found.")