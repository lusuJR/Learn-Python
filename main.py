from employee.employees import get_all_employees


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