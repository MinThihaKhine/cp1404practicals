""" Min Thiha Khine
#14686570

Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many lines of output.
Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS .
• Each line (quick pick) should not contain any repeated number.
• Each line of numbers should be displayed in sorted (ascending) order.
• Study the formatting below so that numbers align"""


import random # import random module

#CONSTANTS
MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45
NUMBER_OF_RANDOM_NUMBERS = 6

number_of_picks = int(input("How many quick picks? ")) # Get number of picks (rows) from user

def main(): #Main Function
    for i in range(number_of_picks):
        random_numbers = generate_picks(NUMBER_OF_RANDOM_NUMBERS, MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        formatted_row = " ".join(f"{number:>{len(str(MAXIMUM_RANDOM_NUMBER))}}" for number in sorted(random_numbers))
        print(formatted_row)

def generate_picks(number, lower_bound, upper_bound ): #Generate random row function
    random_numbers = []
    for i in range(NUMBER_OF_RANDOM_NUMBERS):
        random_number = random.randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        while random_number in random_numbers:
            random_number = random.randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        random_numbers.append(random_number)
    return random_numbers

main() #Code starts here









