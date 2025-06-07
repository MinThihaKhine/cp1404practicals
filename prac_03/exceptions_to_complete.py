"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished =  True  #set is_finished to True to exit the loop if there is no error
    except ValueError:  # To account for invalid input
        print("Please enter a valid integer.")
print("Valid result is:", result)



