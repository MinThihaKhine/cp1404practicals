MINIMUM_PASSWORD_LENGTH = 8

password = input("Enter your password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print(f"Password must be at least {MINIMUM_PASSWORD_LENGTH} characters long ")
    password = input("Enter your password: ")

length_of_password = len(password)
print("*" * length_of_password)