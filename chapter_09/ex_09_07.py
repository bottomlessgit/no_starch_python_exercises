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
    def __init__(self, first_name, last_name, username, age, privileges):
        super().__init__(first_name, last_name, username, age)
        self.privileges = privileges

    def show_privileges(self):
        print("This administrator's prviliges are:")
        for privilege in self.privileges:
            print(privilege)





admin_privileges = ["can add post", "can remove post", "can ban users"]
admin_1 = Admin("martia", "harmartia", "fatalflaw39", 80, admin_privileges)
admin_1.describe_user()
admin_1.show_privileges()




