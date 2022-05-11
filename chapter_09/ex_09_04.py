class Restaurant():
	"""A simple attempt to model a restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant_name, cuisine_type,
		   and number of patrons served"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""Prints restaurant name and cuisine type"""
		print("Restaurant Name: " + self.restaurant_name.title())
		print("Cuisine Type: " + self.cuisine_type)
		print("Number Served: " + str(self.number_served))

	def open_restaurant(self):
		"""Prints statement indicating restaurant is open"""
		print(self.restaurant_name.title() + " is open!")

	def set_number_served(self, new_number_served):
		"""Sets new value for number_served"""
		self.number_served = new_number_served

	def increment_number_served(self, increment):
		"""increments number_served attribute by input value"""
		self.number_served += increment




my_restaurant = Restaurant("Hoch and David", "Cereal and Milk")
my_restaurant.describe_restaurant()
my_restaurant.set_number_served(20)
my_restaurant.describe_restaurant()
my_restaurant.increment_number_served(10)
my_restaurant.describe_restaurant()