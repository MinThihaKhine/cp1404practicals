""" Min Thiha Khine (#14686570)
CP1404/CP5632 Practical
Taxi Simulator - Step by Step Build
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Run the taxi simulator program."""
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = None  # No taxi selected initially
    total_bill = 0.0  # Track total cost

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            pass
        elif choice == "d":
            pass
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>> ").lower()



if __name__ == '__main__':
    main()