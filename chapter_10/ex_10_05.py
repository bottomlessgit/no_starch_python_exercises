file_name = "programming_reasons.txt"
with open(file_name, "w") as file_object:
    reason = ""
    print("We'll be taking a list of reasons people like to program.\n" +
          "Input \"quit\" at any time to exit program.")
    while True:
        reason = input("Input a reason you like programming:\n")
        if reason =="quit":
            break
        file_object.write(reason + "\n")