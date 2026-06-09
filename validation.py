import re


def validate_age(age):
    return age >= 18


def validate_salary(salary):
    return salary > 0


def validate_email(email):

    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    return re.match(pattern, email)


def validate_phone(phone):

    return len(phone) == 10 and phone.isdigit()