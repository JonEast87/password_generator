import random
import string


# These parameters establish the rules that the generator must follow when outputting a password
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    # Next four lines checks if the parameters are true, if they are then they will be added to the letter string
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # Variables created to handle what is included in the password itself
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        # Checks if the newly made character is a digit / special character in it
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        # This compound conditional checks against the earlier conditional and sets meets_criteria accordingly
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd
