# Employee Management System

## Overview

Employee Management System is a Python-based application designed to manage employee records efficiently using MySQL as the backend database. The system provides employee CRUD operations, bulk data import, reporting, analytics, and data visualization features to simplify HR management tasks.

This project demonstrates Python programming, Object-Oriented Programming (OOP), MySQL database integration, data analysis, and reporting capabilities.

---

## Features

### Employee Management

* Add Employee
* View All Employees
* Search Employee by ID
* Search Employee by Name
* Update Employee Salary
* Delete Employee

### Bulk Operations

* Bulk Import Employees from CSV
* Validate Employee Data Before Insertion

### Reports & Analytics

* Department-wise Employee Count
* Average Salary Report
* Highest Paid Employee Report
* Lowest Paid Employee Report
* Employees Joined After a Specific Date

### Data Export

* Export Employee Records to CSV
* Export Employee Records to Excel

### Data Visualization

* Department-wise Employee Count Chart
* Salary Distribution Chart
* Top 10 Highest Paid Employees Chart

---

## Technologies Used

* Python
* MySQL
* Pandas
* Matplotlib
* Object-Oriented Programming (OOP)
* SQL

---

## Project Structure

```text
Employee-Management-System-Python-MySQL/
│
├── main.py
├── database.py
├── employee.py
├── validation.py
├── README.md
├── requirements.txt
└── screenshots/
```

---

## Database Schema

```sql
CREATE TABLE employees(
    emp_id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    department VARCHAR(100),
    designation VARCHAR(100),
    salary DECIMAL(10,2),
    email VARCHAR(100),
    phone VARCHAR(15),
    joining_date DATE
);
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/thanushk7/Employee-Management-System-Python-MySQL.git
```

### Move to Project Directory

```bash
cd Employee-Management-System-Python-MySQL
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure MySQL

Create a database:

```sql
CREATE DATABASE employee_management;
```

Use the database:

```sql
USE employee_management;
```

Create the employees table using the schema provided above.

Update the MySQL connection details in `database.py`:

```python
self.conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="employee_management"
)
```

---

## Running the Application

```bash
python main.py
```

---

## Sample Menu

```text
===== EMPLOYEE MANAGEMENT SYSTEM =====

1. Add Employee
2. View Employees
3. Search Employee By ID
4. Update Salary
5. Delete Employee
6. Exit
7. Bulk Import Employees
8. Search Employee By Name
9. Department Wise Employee Count
10. Average Salary Report
11. Highest Paid Employee
12. Lowest Paid Employee
13. Employees Joined After Date
14. Export Employees to CSV
15. Export Employees to Excel
16. Department Wise Chart
17. Salary Distribution Chart
18. Top 10 Highest Paid Employees Chart
```

---

## Skills Demonstrated

* Python Programming
* Object-Oriented Programming
* MySQL Database Management
* CRUD Operations
* Data Validation
* SQL Queries
* Data Analysis
* Data Visualization
* CSV & Excel Processing
* Git & GitHub

---

## Future Enhancements

* User Authentication
* Role-Based Access Control
* Attendance Management
* Leave Management
* Employee Performance Tracking
* Tkinter GUI Application
* Flask Web Application
* Interactive Dashboard

---

## Author

Thanush K

GitHub: https://github.com/thanushk7
