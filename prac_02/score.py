"""
Min Thiha Khine
(#14686570)

Score status determining program with functions
This program validates and categorizes scores based on predefined ranges.
"""

import random

#CONSTANTS
LOWER_BOUND = 0
UPPER_BOUND = 100
EXCELLENT_SCORE_BOUND = 90
PASS_SCORE_BOUND = 50

def main(): #Main function
    """Get user score and display result then generate random score."""
    # Get user score and print result
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(result)

    # Generate random score and print result
    random_score = random.randint(LOWER_BOUND, UPPER_BOUND)
    result = determine_score_result(random_score)
    print(f"Random score: {random_score}")
    print(result)

def determine_score_result(score):
    """Determine the result category for a given score."""
    if score < LOWER_BOUND or score > UPPER_BOUND:  # Invalid Score
        return "Invalid score"
    elif score >= EXCELLENT_SCORE_BOUND:  # Excellent Score
        return "Excellent"
    elif score >= PASS_SCORE_BOUND:  # Passable Score
        return "Passable"
    else:  # Bad Score
        return "Bad"

main()

