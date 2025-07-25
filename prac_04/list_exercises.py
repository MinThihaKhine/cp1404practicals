"""list_exercises.py
Min Thiha Khine
#14686570
"""
#Constants
NUMBER_OF_PROMPTS = 5
USERNAMES = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
             'bob']  # Change CONSTANT NAME

def main():
    numbers = []
    get_numbers(numbers)
    display_numbers_details(numbers)
    validate_username()

def get_numbers(numbers):
    for i in range(NUMBER_OF_PROMPTS):
        number = int(input("Number: "))
        numbers.append(number)

def display_numbers_details(numbers):
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

def validate_username():
    username = input("Please enter your username:  ")
    if username in USERNAMES:
        print("Access granted")
    else:
        print("Access denied")

main()
