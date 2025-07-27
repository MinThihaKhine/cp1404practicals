""" Min Thiha Khine (#14686570)
CP1404/CP5632 Practical
Taxi Simulator - Complete Version
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
            print("Taxis available:")
            display_taxis(taxis)
            selected_taxi = choose_taxi(taxis)
            if selected_taxi:
                current_taxi = selected_taxi
        elif choice == "d":
            if current_taxi:
                current_taxi.start_fare()
                distance = get_distance()
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    # Final summary when user quits
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    """Display all taxis with their current status."""
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


def choose_taxi(taxis):
    """Get taxi selection from user and handle invalid choices."""
    try:
        taxi_choice = int(input("Choose taxi: "))
        return taxis[taxi_choice]
    except (ValueError, IndexError):
        print("Invalid taxi choice")
        return None


def get_distance():
    """Get valid distance input from user with error handling."""
    MINIMUM_DISTANCE = 0
    while True:
        try:
            distance = float(input("Drive how far? "))
            if distance >= MINIMUM_DISTANCE:
                return distance
            else:
                print("Distance must be positive")
        except ValueError:
            print("Invalid distance")

if __name__ == '__main__':
    main()