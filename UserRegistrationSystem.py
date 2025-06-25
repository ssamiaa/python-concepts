#Objective: Simulate a user registration system that handles input errors using exceptions.
# Custom exception classes
class InvalidUsernameError(Exception):
    pass

class UnderageError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

# --- Username Validation ---
try:
    username = input("Enter username (at least 5 characters): ")
    if len(username) < 5:
        raise InvalidUsernameError("Username must be at least 5 characters long.")
except InvalidUsernameError as ue:
    print("Username must be at least 5 characters long.")
    username = None

# --- Age Validation ---
try:
    age_input = input("Enter age (must be ≥ 18): ")
    age = int(age_input)
    if age < 18:
        raise UnderageError("User must be at least 18 years old.")
except ValueError:
    print("Please enter a valid integer for age.")
    age = None
except UnderageError as ue:
    print("User must be at least 18 years old.")
    age = None

# --- Email Validation ---
try:
    email = input("Enter email (must contain '@' and '.'): ")
    if '@' not in email or '.' not in email:
        raise InvalidEmailError("Email must contain '@' and '.'")
except InvalidEmailError as ee:
    print("Email must contain '@' and '.'")
    email = None

# --- Final Check ---
if username and age and email:
    print("Registration successful!")
else:
    print("Registration failed. Please fix the errors and try again.")
