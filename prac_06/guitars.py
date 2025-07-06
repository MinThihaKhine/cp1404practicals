"""
Estimated: 20 minutes
Actual:  minutes
"""

from prac_06.guitar import Guitar

MINIMUM_NUMBER = 0

def main():
    """Ask for guitar details :name, year and cost, until blank is entered then output all details"""
    guitars = []
    print("My guitars!")

    name = input("Name: ").strip()
    while name != "":
        year = int(get_valid_number("Year: "))
        cost = get_valid_number("Cost: $")

        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.\n")
        name = input("Name: ").strip()

def get_valid_number(prompt):
    """Get any valid positive number (int or float)."""
    is_valid = False

    while not is_valid:
        try:
            number = float(input(prompt))
            if number > MINIMUM_NUMBER:
                is_valid = True
            print("Number must be positive")
        except ValueError:
            print("Please enter a proper number")
    return number




main()
