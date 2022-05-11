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


class IceCreamStand(Restaurant):
	"""An ice cream stand extnesion of the restaurant class"""
	def __init__(self, restaurant_name, cuisine_type, flavor_list):
		"""initiatializes Restaurant attributes and flavor_list"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavor_list = flavor_list

	def add_flavor(self, new_flavor):
		"""Adds a flavor to flavor_list attribute"""
		self.flavor_list.append(new_flavor)

	def list_flavors(self):
		"""Prints list of flavors offered"""
		print("The list of ice cream flavors is: ")
		for flavor in self.flavor_list:
			print(flavor)

#statement to prevent running when this module is imported
if __name__ == "__main__":
	yummy_flavors = ["chocolate", "vanilla", "caramel", "strawberry", "cookies and cream"]
	billy_frost_ice_creams = IceCreamStand("BiFrost Creams", "Standard Ice Cream", yummy_flavors)
	billy_frost_ice_creams.describe_restaurant()
	billy_frost_ice_creams.list_flavors()
