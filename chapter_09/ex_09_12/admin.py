import user 
class Admin(user.User):
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