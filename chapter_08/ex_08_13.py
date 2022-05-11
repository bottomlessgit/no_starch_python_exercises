def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user.""" 
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('Le', 'Narc', attitude='spicy',
							 coding_skills="ehhhhhhh... he's alright",
							 sunny_disposition=True)
print(user_profile)