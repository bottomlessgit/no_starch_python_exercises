def make_car(manufacturer, model_name, **other_features):
	"""builds a dictionary representing a car with the given input"""
	car = {'manufacturer': manufacturer, 'model_name': model_name}
	for feature_key, feature_value in other_features.items():
		car[feature_key] = feature_value
	return car

new_car = make_car('Honda', 'Civic', color='gold', mileage=525601)
print(new_car)
