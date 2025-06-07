"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0: # Modified code to avoid ZeroDivisionError by checking denominator before division
        print("Cannot divide by zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")


""" Answers to Questions 1 , 2, 3 - 

1. A ValueError occurs when the user enters something that cannot be converted to an integer,
   such as a string or text like "hello", empty input, or decimal numbers/float like "3.5"

2. A ZeroDivisionError occurs when the user enters 0 as the denominator, since division by zero
   is mathematically undefined 

3. Yes, we can avoid ZeroDivisionError by checking if the denominator is zero before performing
   the division and asking for a new denominator through a validation check.
"""