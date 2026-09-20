from employee.employees import (
    add_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    delete_employee
)


while True:

    print("\n====================================")
    print("     EMPLOYEE MANAGEMENT SYSTEM")
    print("====================================")

    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("0. Exit")

    choice = input("\nSelect an option: ")


    # CREATE
    if choice == "1":

        print("\n========== ADD EMPLOYEE ==========")

        name = input("Enter employee full name: ")
        department = input("Enter department: ")
        salary = float(input("Enter salary: R"))

        add_employee(
            name,
            department,
            salary
        )


    # READ
    elif choice == "2":

        print("\n========== EMPLOYEE LIST ==========")

        employees = get_all_employees()

        if len(employees) == 0:

            print("No employees found.")

        else:

            for employee in employees:

                print(f"\nEmployee ID : {employee[0]}")
                print(f"Name        : {employee[1]}")
                print(f"Department  : {employee[2]}")
                print(f"Salary      : R {employee[3]:.2f}")

                print("--------------------------------")


    # SEARCH
    elif choice == "3":

        print("\n========== SEARCH EMPLOYEE ==========")

        employee_id = int(
            input("Enter Employee ID: ")
        )

        employee = get_employee_by_id(employee_id)

        if employee:

            print("\nEmployee Found!")

            print(f"Employee ID : {employee[0]}")
            print(f"Name        : {employee[1]}")
            print(f"Department  : {employee[2]}")
            print(f"Salary      : R {employee[3]:.2f}")

        else:

            print("\nEmployee not found.")


    # UPDATE
    elif choice == "4":

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
            salary = float(
                input("Enter new salary: R")
            )

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


    # DELETE
    elif choice == "5":

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

                rows_deleted = delete_employee(
                    employee_id
                )

                if rows_deleted > 0:

                    print("\nEmployee deleted successfully!")

            else:

                print("\nDelete cancelled.")

        else:

            print("\nEmployee not found.")


    # EXIT
    elif choice == "0":

        print(
            "\nThank you for using the "
            "Employee Management System."
        )

        break


    # INVALID OPTION
    else:

        print("\nInvalid option. Please try again.")
