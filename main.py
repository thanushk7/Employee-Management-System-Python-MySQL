from database import Database
from employee import Employee
from validation import *

db = Database()

while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Bulk Import Employees")
    print("7. Search Employee By Name")
    print("8. Department Wise Employee Count")
    print("9. Average Salary Report")
    print("10. Highest Paid Employee")
    print("11. Lowest Paid Employee")
    print("12. Employees Joined After Date")
    print("13. Export Employees to CSV")
    print("14. Export Employees to Excel")
    print("15. Department Wise Chart")
    print("16. Salary Distribution Chart")
    print("17. Top 10 Highest Paid Employees Chart")
    print("18. Exit")


    choice = input("Enter Choice: ")

    if choice == "1":

        emp_id = int(input("Employee ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        department = input("Department: ")
        designation = input("Designation: ")
        salary = float(input("Salary: "))
        email = input("Email: ")
        phone = input("Phone: ")
        joining_date = input("Joining Date (YYYY-MM-DD): ")

        if not validate_age(age):
            print("Invalid Age")
            continue

        if not validate_salary(salary):
            print("Invalid Salary")
            continue

        if not validate_email(email):
            print("Invalid Email")
            continue

        if not validate_phone(phone):
            print("Invalid Phone")
            continue

        emp = Employee(
            emp_id,
            name,
            age,
            gender,
            department,
            designation,
            salary,
            email,
            phone,
            joining_date
        )

        try:
            db.add_employee(emp)
            print("Employee Added Successfully")

        except Exception as e:
            print("Error:", e)

    elif choice == "2":

        employees = db.view_employees()

        print("\nEmployee Records")
        print("-" * 80)

        for emp in employees:
            print(emp)

    elif choice == "3":

        emp_id = int(input("Enter Employee ID: "))

        result = db.search_employee(emp_id)

        if result:
            print(result)
        else:
            print("Employee Not Found")

    elif choice == "4":

        emp_id = int(input("Employee ID: "))
        salary = float(input("New Salary: "))

        db.update_salary(emp_id, salary)

        print("Salary Updated Successfully")

    elif choice == "5":

        emp_id = int(input("Employee ID: "))

        db.delete_employee(emp_id)

        print("Employee Deleted Successfully")

    
    elif choice == "6":
        file_path = input("Enter CSV file path: ")
        db.bulk_insert(file_path)
    
    elif choice == "7":
        name = input("Enter Employee Name: ")
        result = db.search_by_name(name)

        if result:
            for row in result:
                print(row)
        else:
            print("No Employee Found")

    elif choice == "8":

        report = db.department_report()

        print(
            "\nDepartment Report"
        )

        for dept, count in report:

            print(
                f"{dept} : {count}"
            )
    elif choice == "9":

        avg = db.average_salary()

        print(
            f"Average Salary: ₹{avg[0]:,.2f}"
        )
    elif choice == "10":

        emp = db.highest_salary_employee()

        print(
            "\nHighest Paid Employee"
        )

        print(emp)
    elif choice == "11":

        emp = db.lowest_salary_employee()

        print(
            "\nLowest Paid Employee"
        )

        print(emp)
    elif choice == "12":

        date = input(
            "Enter Date (YYYY-MM-DD): "
        )

        result = db.joined_after(date)

        for row in result:
            print(row)
    elif choice == "13":
        db.export_csv()
    elif choice == "14":
        db.export_excel()
    elif choice == "15":
        db.department_chart()

    elif choice == "16":
        db.salary_chart()

    elif choice == "17":
        db.top_10_salary_chart()

    elif choice == "18":

        db.close()
        print("Thank You")
        break

    else:
        print("Invalid Choice")