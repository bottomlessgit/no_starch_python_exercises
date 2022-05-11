name = input("Please input your full name.")
with open("guest.txt", "w") as dort:
    dort.write(name)