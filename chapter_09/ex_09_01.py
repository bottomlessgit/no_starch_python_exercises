class Restaurant():
	"""A simple attempt to model a restaurant"""
	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize restaurant_name and cuisine_type attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""print restaurant name and cuisine type"""
		print("Restaurant Name: " + self.restaurant_name.title())
		print("Cuisine Type: " + self.cuisine_type)

	def open_restaurant(self):
		print(self.restaurant_name.title() + " is open!")


my_restaurant = Restaurant("Hoch and David", "Cereal and Milk")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()