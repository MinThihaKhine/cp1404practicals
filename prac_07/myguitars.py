import csv

from prac_07.guitar import Guitar


FILENAME = "guitars.csv"

def main():
    guitars = read_guitars(FILENAME)  # Read guitars from file


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






