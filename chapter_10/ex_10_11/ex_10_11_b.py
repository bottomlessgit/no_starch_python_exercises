import json

filename = "favorite_number.json"
try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)
        msg = "I know your favorite number! It's " + str(favorite_number)
        print(msg)
except FileNotFoundError:
    print(filename + " file not found.")