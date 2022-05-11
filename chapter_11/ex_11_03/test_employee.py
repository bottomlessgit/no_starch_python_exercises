import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """tests for the class Employee"""

    def setUp(self):
        """Create an employee and a custom raise for use in all test methods"""
        first_name = "John"
        last_name = "Doe"
        salary = 50000
        self.my_employee = Employee(first_name, last_name, salary)
        self.custom_raise = 10000

    def test_default_raise(self):
        """Test that give_raise function with no input gives default raise"""
        default_raise = 5000
        new_salary = self.my_employee.salary + default_raise
        self.my_employee.give_raise()  
        self.assertEqual(new_salary, self.my_employee.salary)

    def test_custom_raise(self):
        """Test that give_raise function with custom input gives custom raise"""
        new_salary = self.my_employee.salary + self.custom_raise
        self.my_employee.give_raise(self.custom_raise)
        self.assertEqual(new_salary, self.my_employee.salary)


unittest.main()

