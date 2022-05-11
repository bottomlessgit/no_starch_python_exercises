import json

with open("favorite_number.json", "w") as f_obj:
    while True:
        try:
            fave_number = int(input("Input your favorite integer\n"))
            json.dump(fave_number, f_obj)
            break
        except ValueError:
            print("That is not an integer, please try again.\n")

