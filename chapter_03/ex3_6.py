guest_list = ["me", "myself", "I"]
for i in range(len(guest_list)):
	print("Hey " + guest_list[i].title() + ", would you like to come to dinner?")
print(guest_list[1].title() + " can't make it.")
guest_list[1] = "the man in the mirror"
for i in range(len(guest_list)):
	print("Hey " + guest_list[i].title() + ", would you like to come to dinner?")

print("Oh wait, we found a bigger table, and since table size is the only constraint for dinner size, let\'s invite more poeple.")
guest_list.insert(0, "yours truly")
guest_list.insert(len(guest_list)//2, "my person")
guest_list.append("\"my college roommate\"")
for i in range(len(guest_list)):
	print("Hey " + guest_list[i].title() + ", would you like to come to dinner?")
