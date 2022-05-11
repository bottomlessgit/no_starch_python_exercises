class User():
    """Simple class to model a user"""
    def __init__(self, first_name, last_name, username, age):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """prints information about the user"""
        print("First Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        print("Username: " + self.username.title())
        print("Age: " + str(self.age))
        print("Login Attempts: " + str(self.login_attempts))
        print()

    def greet_user(self):
        """Prints greeting to use with user's name"""
        print("Hello " + self.first_name.title() + " " + 
              self.last_name.title() + ", welcome!")

    def increment_login_attempts(self):
        """increments login_attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets login_attempts to 0"""
        self.login_attempts = 0


class Admin(User):
    """Extension of User class that has admin privileges"""
    def __init__(self, first_name, last_name, username, age):
        super().__init__(first_name, last_name, username, age)
        self.privileges = Privileges()


class Privileges():
    """Class to contain a list of user privileges"""
    def __init__(self):
        """Initialize privilege list"""
        self.privilege_list = []

    def set_privilege_list(self, new_privilege_list):
        """set new privilege list to copy of input list"""
        self.privilege_list = new_privilege_list[:]

    def add_privilege(self, new_privilege):
        """Adds a privilege to the privilege list"""
        self.privilege_list.append(new_privilege)


    def show_privileges(self):
        """Prints list of privileges"""
        print("List of privileges:")
        for privilege in self.privilege_list:
            print("\t-" + privilege)