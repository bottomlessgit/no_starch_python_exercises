def print_file(filename):
    """prints content of .txt file"""
    try:
        with open(filename) as file_object:
            print(file_object.read().rstrip())
    except FileNotFoundError:
        pass

filename_1 = "cats.txt"
print_file(filename_1)

filename_2 = "dogs.txt"
print_file(filename_2)