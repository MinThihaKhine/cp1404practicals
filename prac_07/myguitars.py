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
    print("\nAdd your new guitars below ")
    new_guitars = get_new_guitars()




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
            print("Invalid number! Please enter a proper number.")



if __name__ == '__main__':
    main()