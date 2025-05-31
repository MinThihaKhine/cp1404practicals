"""
Score menu program with validation and display options
Users can get valid scores, view score results, display stars, and quit.

This program provides a menu interface for :
    (G)et a valid score (must be 0-100 inclusive)
    (P)rint result (copy or import your function to determine the result from score.py)
    (S)how stars (this should print as many stars as the score)
    (Q)uit

Min Thiha Khine (#14686570)
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


def main(): #Main Function
    """Display menu and handle score operations until user quits."""
    score = get_valid_score()  # Initial setup before menu

    # Display menu and get choice
    print(MENU)
    choice = input(">>> ").upper()
    # Choice loop as long as user doesn't quit (Q)
    while choice != 'Q':  # Repeat this block of code unless user enters Q
        if choice == "G": # Get valid score
            score = get_valid_score()
        elif choice == "P": # Print result for a given score
            result = determine_score_result(score)
            print(result)
        elif choice == "S": # Print stars equal to the score value.
            show_stars(score)
        else: # Invalid choice message
            print("Invalid option")

        # Display Menu again and get new choice
        print("\n", MENU, sep = "") #Clean output
        choice = input(">>> ").upper()
    print("Farewell my dear user ;-;")  #Finished message


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


main() # The program starts here