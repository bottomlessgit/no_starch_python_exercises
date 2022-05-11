class Employee():
    """Records full name and annual salary of an employee"""

    def __init__(self, first_name, last_name, salary):
        """initializes employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        """returns formatted full name"""
        full_name = self.first_name.title() + " " + self.last_name.title()
        return full_name

    def give_raise(self, s_raise = 5000):
        """raises salary by input increment or default of 5000"""
        self.salary += s_raise


