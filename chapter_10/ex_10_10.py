def count_word_in_text(book_filename, target_word):
    """counts the number of times a word appears in a given file"""
    try:
        with open(book_filename) as file_object:

            word_count = file_object.read().lower().count(target_word)
            result_msg = (book_filename + " has " + str(word_count) +
                          " instances of the word " + target_word)
            print(result_msg)
    except FileNotFoundError:
            error_msg = book_filename + " not found."
            print(error_msg)

book_filenames = ["the_metamorphosis.txt", "alices_adventures_in_wonderland.txt"]
target_word = "the"
for book_filename in book_filenames:
    count_word_in_text(book_filename, target_word)
