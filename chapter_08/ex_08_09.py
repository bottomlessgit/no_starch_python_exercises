def show_magicians(magician_list):
	"""Prints magicians names with polite message"""
	for magician in magician_list:
		print(magician.title(), "is a great Magician")

magicians = ["faye presto", "ben barnes", "harry houdini", "david blaine"]
show_magicians(magicians)