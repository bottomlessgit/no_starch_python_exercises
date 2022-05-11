def show_magicians(magician_list):
	"""Prints magicians names with polite message"""
	for magician in magician_list:
		print(magician.title(), "is a great Magician")

def make_great(magician_list):
	"""Adds 'the great' to the beginning of each item of a list """
	for i in range(len(magician_list)):
		magician_list[i] = "the great " + magician_list[i]

magicians = ["faye presto", "ben barnes", "harry houdini", "david blaine"]
make_great(magicians)
show_magicians(magicians)