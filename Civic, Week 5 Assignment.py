# Password Policy Checker
# This program will check your inputted password against the requirements of the Password Policy. 
# Name: Adnan Civic
# Date: 2/19/2024

# Password Policy:
# - Length between 8-20
# - Contains at least one digit
# - Contains at least one alphabetic character
# - Does not contain spaces

# Setting password Min and Max length.
def is_valid_length(password, min_length=8, max_length=20):
    return min_length <= len(password) <= max_length

# Setting one digit and alphabetic character requirements.
# Both has_digit
def contains_required_characters(password):
    has_digit = False
    has_alpha = False
    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isalpha():
            has_alpha = True
    return has_digit and has_alpha

# Excluding spaces from password.
def no_prohibited_characters(password):
    return ' ' not in password

# Validate the password based on defined criteria.
# Return True if valid, else False and print specific error message.
def validate_password(password):
    
    if not is_valid_length(password):
        print("Invalid password: Length is not within the allowed range.")
        return False
    if not contains_required_characters(password):
        print("Invalid password: Must contain at least one digit and one alphabetic character.")
        return False
    if not no_prohibited_characters(password):
        print("Invalid password: Contains prohibited characters (spaces).")
        return False
    print("Password is valid.")
    return True

# Main program
if __name__ == "__main__":
    while True:
        user_password = input("Enter a password to check if it meets the Password Policy: ")
        if validate_password(user_password):
            break  # Password is valid, exit the loop
        else:
            print("Please try again.")
