# Importing pytest module for writing unittests
# Importing main module which contains the various functions related to an Employee

import pytest
from main import *

# Creating Global Objects
employee_1 = create_employee_profile('Steve', 'Gates', date(1999, 1, 8), 50000, 'Technical')
employee_2 = create_employee_profile('Suyash', 'Singh', date(1995, 4, 22), 60000, 'Electrical')

# Note: All the functions need to start with 'test_' or else it will be ignored

def test_increementSalary():
    assert increase_employee_salary(employee_1, 30) == 65000

def test_getAge():
    assert get_age(employee_1) == 23

# Checks if the user is in valid department
def test_getDepartment():
    assert get_department(employee_2) in Employee.departments

# This function will be ignored by pytest as it does not begin with 'test_'
def checkEmailId():
    assert get_email(employee_2) == 'Suyash.Singh@gmail.com'
    e2.l_name = ''
    assert get_email(employee_2) == 'Suyash.Singh@gmail.com'


