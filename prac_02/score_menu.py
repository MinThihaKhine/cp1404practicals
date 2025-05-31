"""
Write a complete Python program following the standard structure that uses a main and other functions.
Use a main menu following the standard menu pattern.

The menu should have four separate options:

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
Handle each of these (except quit) separately, and consider how you can reuse your functions.

In main(), before the menu loop, get a valid score using your function.
When the user quits, say some kind of "farewell".
"""

# CONSTANTS
LOWER_BOUND = 0
UPPER_BOUND = 100
EXCELLENT_SCORE_BOUND = 90
PASS_SCORE_BOUND = 50

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Display menu and handle score operations until user quits."""

def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    score = float(input(f"Enter score ({LOWER_BOUND} - {UPPER_BOUND}): "))
    while score < LOWER_BOUND or score > UPPER_BOUND:
        print(f"Invalid score. Must be between {LOWER_BOUND} and {UPPER_BOUND} inclusive.")
        score = float(input(f"Enter score ({LOWER_BOUND} - {UPPER_BOUND}): "))
    return score

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

def show_stars(score):
    """Print stars equal to the score value."""
    print("*" * int(score))




# main()


# get_valid_score()