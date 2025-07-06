"""
Estimated: 20 minutes
Actual:  minutes
"""

from prac_06.guitar import Guitar

def main():
    """Ask for guitar details :name, year and cost, until blank is entered then output all details"""
    guitars = []
    print("My guitars!")

    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))

        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("Name: ").strip()
