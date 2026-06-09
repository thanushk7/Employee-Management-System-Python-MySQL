import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


class Database:

    def __init__(self):

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ga7@Ma0#",
            database="employee_management"
        )

        self.cursor = self.conn.cursor()

    def add_employee(self, employee):

        query = """
        INSERT INTO employees
        (emp_id,name,age,gender,department,
        designation,salary,email,phone,joining_date)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        values = (
            employee.emp_id,
            employee.name,
            employee.age,
            employee.gender,
            employee.department,
            employee.designation,
            employee.salary,
            employee.email,
            employee.phone,
            employee.joining_date
        )

        self.cursor.execute(query, values)
        self.conn.commit()

    def view_employees(self):

        self.cursor.execute("SELECT * FROM employees")
        return self.cursor.fetchall()

    def search_employee(self, emp_id):

        query = "SELECT * FROM employees WHERE emp_id=%s"

        self.cursor.execute(query, (emp_id,))
        return self.cursor.fetchone()

    def update_salary(self, emp_id, salary):

        query = """
        UPDATE employees
        SET salary=%s
        WHERE emp_id=%s
        """

        self.cursor.execute(query, (salary, emp_id))
        self.conn.commit()

    def delete_employee(self, emp_id):

        query = """
        DELETE FROM employees
        WHERE emp_id=%s
        """

        self.cursor.execute(query, (emp_id,))
        self.conn.commit()
    def bulk_insert(self, file_path):
        df = pd.read_csv(file_path)
        query = """
        INSERT INTO employees
        (emp_id,name,age,gender,department,
        designation,salary,email,phone,joining_date)
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """

        data = [tuple(row) for row in df.values]

        self.cursor.executemany(query, data)
        self.conn.commit()

        print(f"{len(data)} Employees Added Successfully")

    def search_by_name(self, name):

        query = """
        SELECT *
        FROM employees
        WHERE name LIKE %s
        """

        self.cursor.execute(
            query,
            (f"%{name}%",)
        )

        return self.cursor.fetchall()
    
    def department_report(self):

        query = """
        SELECT department,
             COUNT(*)
        FROM employees
        GROUP BY department
        """

        self.cursor.execute(query)

        return self.cursor.fetchall()
    
    def average_salary(self):

        query = """
        SELECT AVG(salary)
        FROM employees
        """

        self.cursor.execute(query)

        return self.cursor.fetchone()
    
    def highest_salary_employee(self):

        query = """
        SELECT *
        FROM employees
        ORDER BY salary DESC
        LIMIT 1
        """

        self.cursor.execute(query)

        return self.cursor.fetchone()
    
    def lowest_salary_employee(self):

        query = """
        SELECT *
        FROM employees
        ORDER BY salary ASC
        LIMIT 1
        """

        self.cursor.execute(query)

        return self.cursor.fetchone()
    
    def joined_after(self, date):

        query = """
        SELECT *
        FROM employees
        WHERE joining_date > %s
        """

        self.cursor.execute(
            query,
            (date,)
        )

        return self.cursor.fetchall()
    def export_csv(self):

        query = """
        SELECT *
        FROM employees
        """

        df = pd.read_sql(query, self.conn)

        df.to_csv(
        "employee_report.csv",
        index=False
        )

        print(
        "CSV Exported Successfully"
        )
    def export_excel(self):

        query = """
    SELECT *
    FROM employees
    """

        df = pd.read_sql(query, self.conn)

        df.to_excel(
        "employee_report.xlsx",
        index=False
    )

        print(
        "Excel Exported Successfully"
    )
    def department_chart(self):

        query = """
        SELECT department,
           COUNT(*)
        FROM employees
        GROUP BY department
        """

        self.cursor.execute(query)

        data = self.cursor.fetchall()

        departments = [
            row[0]
            for row in data
    ]

        counts = [
            row[1]
            for row in data
    ]

        plt.figure(figsize=(8,5))

        plt.bar(
            departments,
            counts
    )

        plt.title(
        "Employees by Department"
    )

        plt.xlabel(
        "Department"
    )

        plt.ylabel(
        "Employee Count"
    )

        plt.show()
    def salary_chart(self):

        query = """
        SELECT salary
        FROM employees
        """

        self.cursor.execute(query)

        data = self.cursor.fetchall()

        salaries = [
            row[0]
            for row in data
    ]

        plt.figure(figsize=(8,5))

        plt.hist(
        salaries,
        bins=10
    )

        plt.title(
        "Salary Distribution"
    )

        plt.xlabel(
        "Salary"
    )

        plt.ylabel(
        "Number of Employees"
    )

        plt.show()

    def top_10_salary_chart(self):

        query = """
        SELECT name,salary
        FROM employees
        ORDER BY salary DESC
        LIMIT 10
        """

        self.cursor.execute(query)

        data = self.cursor.fetchall()

        names = [
        row[0]
        for row in data
    ]

        salaries = [
        row[1]
        for row in data
    ]

        plt.figure(figsize=(10,5))

        plt.bar(
        names,
         salaries
    )

        plt.title(
        "Top 10 Highest Paid Employees"
    )

        plt.xticks(rotation=45)

        plt.show()

    def close(self):
        self.conn.close()