def show_magicians(magician_list):
	"""Prints magicians names with polite message"""
	for magician in magician_list:
		print(magician.title(), "is a great Magician")

def make_great(magician_list):
	"""returns a new list with 'the great' added to the beginning of each element"""
	for i in range(len(magician_list)):
		magician_list[i] = "the great " + magician_list[i]
	return magician_list


magicians = ["faye presto", "ben barnes", "harry houdini", "david blaine"]
great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)


def build_profile(first, last, **yort)