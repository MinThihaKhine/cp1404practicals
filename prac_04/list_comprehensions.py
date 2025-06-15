"""

Write a program that asks the user how many "quick picks" they wish to generate. The program then generates that many lines of output.
Each line consists of 6 random numbers between 1 and 45.
These values should be stored as CONSTANTS .
• Each line (quick pick) should not contain any repeated number.
• Each line of numbers should be displayed in sorted (ascending) order.
• Study the formatting below so that numbers align


"""

import random

MINIMUM_RANDOM_NUMBER = 1
MAXIMUM_RANDOM_NUMBER = 45
NUMBER_OF_RANDOM_NUMBERS = 6

# number_of_picks = int(input("How many quick picks? "))

random_numbers = []
for i in range(NUMBER_OF_RANDOM_NUMBERS):
    random_number = random.randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
    while random_number in random_numbers:
        random_number = random.randint(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
    random_numbers.append(random_number)
print(random_numbers)

