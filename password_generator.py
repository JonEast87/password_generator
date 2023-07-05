import random
import string


# These parameters establish the rules that the generator must follow when outputting a password
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    print(letters, digits, special)


generate_password(10)
