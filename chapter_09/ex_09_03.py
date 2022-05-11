class User():
	"""Simple class to model a user"""
	def __init__(self, first_name, last_name, username, age):
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.age = age

	def describe_user(self):
		"""prints information about the user"""
		print("First Name: " + self.first_name.title())
		print("Last Name: " + self.last_name.title())
		print("Username: " + self.username.title())
		print("Age: " + str(self.age))

	def greet_user(self):
		"""Prints greeting to use with user's name"""
		print("Hello " + self.first_name.title() + " " + 
			  self.last_name.title() + ", welcome!")

user_1 = User("martia", "harmartia", "fatalflaw39", 80)
user_2 = User("robert", "flobert", "RobTheFlob", 29)
user_3 = User("dennis", "menace", "NicePerson82", 39)

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
