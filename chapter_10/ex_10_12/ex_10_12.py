import json

def get_stored_fnumber():
    """Returns stored value for favorite number from file"""
    filename = "favorite_number.json"
    try:
        with open(filename) as f_obj:
            fave_number = json.load(f_obj)
    except FileNotFoundError:
            return None
    else:
        return fave_number

def get_new_fnumber():
    """prompts user for new fnumber and stores it in file"""
    while True:
        try:
            fave_number = int(input("Input your favorite integer\n"))
            break
        except ValueError:
            print("That is not an integer, please try again.\n") 

    filename = "favorite_number.json"
    with open(filename, "w") as f_obj:
        json.dump(fave_number, f_obj)

    return fave_number

def new_number_message():
    """Calls function for new number and prints message to user"""
    favorite_number = get_new_fnumber()
    msg = ("We'll remember your favorite number is " +  
           str(favorite_number) + " when you come back.")
    print(msg)

def process_favorite_number():
    favorite_number = get_stored_fnumber()
    if favorite_number:
        msg = "Your favorite number is: " + str(favorite_number)
        print(msg)
        new_number_prompt = ("input y if you'd like to choose a new "
                             "favorite number, input anything else otherwise.\n")
        wants_new_fnumber = input(new_number_prompt)
        if wants_new_fnumber == "y":
            new_number_message()
    else:
        new_number_message()

process_favorite_number()
