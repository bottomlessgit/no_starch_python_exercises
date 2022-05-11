guest_list = ["me", "myself", "I"]
for i in range(len(guest_list)):
	print("Hey " + guest_list[i].title() + ", would you like to come to dinner?")
print(guest_list[1].title() + " can't make it.")
guest_list[1] = "the man in the mirror"
for i in range(len(guest_list)):
	print("Hey " + guest_list[i].title() + ", would you like to come to dinner?")
