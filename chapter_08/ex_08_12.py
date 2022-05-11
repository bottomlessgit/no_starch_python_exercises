def sandwich_summary(*fillings):
	"""describes sandwich made of inputted fillings"""
	print("Your sandwich has the following fillings:")
	for filling in fillings:
		print("\t-" + filling)

sandwich_summary("lettuce", "tomatoes", "pickles")
sandwich_summary("blue cheese", "green cheese", "the cheese knees")
sandwich_summary("a whole lot of nothing")
