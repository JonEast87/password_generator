import random
import string


# These parameters establish the rules that the generator must follow when outputting a password
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    # Next four lines checks if the parameters are true, if they are then they will be added to the letters list
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False


generate_password(10)
