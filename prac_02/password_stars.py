"""
Min Thiha Khine
#14686570
Asterisks printing based on validated password length with a function based structure
"""

MINIMUM_PASSWORD_LENGTH = 8 #Constant

def main(): #Main Function
    """Get valid password and asterisks based on password length"""
    password = get_password()
    print_asterisks(password)

def get_password(): # Get valid password from user
    """Get password that meets the minimum length validation """
    password = input("Enter your password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Password must be at least {MINIMUM_PASSWORD_LENGTH} characters")
        password = input("Enter your password: ")
    return password

def print_asterisks(password):
    """Print asterisks matching the length of the password"""
    length_of_password = len(password) # Stores the length of the password
    asterisks = '*' * length_of_password # Stores the total asterisks (Good code practice)
    print(asterisks)

main() # The main function starts here
