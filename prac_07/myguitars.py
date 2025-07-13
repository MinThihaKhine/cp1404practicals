"""Min Thiha Khine (#14686570)"""
from prac_07.guitar import Guitar


FILENAME = "guitars.csv"

def main():
    """Read guitars data and ask user to add more back to file"""
    guitars = read_guitars(FILENAME)
    print(f"Imported {len(guitars)} from {FILENAME}")
    print("My Guitars!")

    # Sort guitars by year and display
    guitars.sort()
    print("\nThese are my guitars sorted by year (oldest to newest):")
    display_guitars(guitars)

    # Get new guitars from user
    print("\nEnter guitar details (press Enter for empty name to stop):")
    new_guitars = get_new_guitars()

    # Add new guitars to collection
    for guitar in new_guitars:
        guitars.append(guitar)

    # Sort and display final collection
    guitars.sort()
    print(f"\nThese are my current guitars:")
    display_guitars(guitars)

    # Write all guitars back to file
    write_guitars_to_file(FILENAME, guitars)
    print(f"Wrote {len(guitars)} guitars to {FILENAME}")


def read_guitars(filename):
    """Read guitar data from CSV file and return list of Guitar objects"""
    guitars = []
    try:
        with open(filename, 'r') as infile:
            for line in infile:
                line = line.strip()
                if line:  # Skip empty lines
                    parameters = line.split(',')
                    if len(parameters) == 3:
                        name, year, cost = parameters
                        guitar = Guitar(name, int(year), float(cost))
                        guitars.append(guitar)
    except FileNotFoundError:
        print(f"File {filename} not found")
    return guitars


def display_guitars(guitars):
    """Display all guitars in the list with numbers."""
    for i, guitar in enumerate(guitars, 1):
        print(f"Guitar {i}: {guitar}")

def get_new_guitars():
    """Get new guitar information from user input."""
    guitars = []

    name = input("Guitar name: ").strip()
    while name != "":
        year = int(get_valid_number("Year: "))
        cost = get_valid_number("Cost: $")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"Guitar added: {guitar}")
        name = input("Guitar name: ").strip()
    return guitars




def get_valid_number(prompt):
    """Validate input to get proper number"""
    is_valid = False

    while not is_valid:
        try:
            number = float(input(prompt))
            if number > 0:
                is_valid = True
            else:
                print("Invalid input! Please enter valid numbers.")
        except ValueError:
            print("Value Error; Please enter a proper number.")
    return number

def write_guitars_to_file(filename, guitars):
    """Write guitars to CSV file"""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

if __name__ == '__main__':
    main()