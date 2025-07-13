
from prac_07.guitar import Guitar


FILENAME = "guitars.csv"

def main():
    print("My Guitars!")
    guitars = read_guitars(FILENAME)

    display_guitars(guitars)

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



if __name__ == '__main__':
    main()