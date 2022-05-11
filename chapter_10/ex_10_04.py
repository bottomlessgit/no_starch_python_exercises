file_name = "guest_book.txt"
with open(file_name, "w") as file_object:
    name = ""
    print("We are going to input names to a guestbook one at a time.\n" + 
          "input \"quit\" at any point to exit.")
    while True:
        name = input("Input a full name: ")
        if name == "quit":
            break
        file_object.write(name + "\n")


