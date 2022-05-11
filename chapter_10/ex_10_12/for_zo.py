import random
#I don't really get your teachers distinction between animate and inanimate
animate_objects = [
    "Cow that jumped over the moon", "the tortoise", "the hare",
    "three kids in a trenchcoat", "a turkey", "Ruvi Rivlin in a trenchcoat",
]
inanimate_objects = [
    "The moon", "Ruvi Rivlin's trenchcoat", "a bar of chocolate",
    "Thanksgiving dinner", "chairs", "tables", 
]

"""now I'll choose to get an element choosing which list randomly
both lists are length 6, I didn't randomize which element from a
given list I chose, I only randomized which list to take from"""
for i in range(6):
    random_num = random.randint(0,1)        #either 0 or 1
    print("Since our random number is " + str(random_num) + 
          ", we choose element " + str(i) + " from list ")
    if random_num == 0:
        print("animate_objects, which is " + animate_objects[i])
    else:
        print("inanimate_objects, which is " + inanimate_objects[i])


