"""
Wimbledon
Estimate: 15 minutes
Actual:      minutes
"""

FILENAME = "wimbledon.csv"


FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

def main():
    """Coordinate the reading, processing and display of Wimbledon data."""
    records = load_records(FILENAME)


def load_records(filename):
    """Read CSV file and return championship data as a list of lists."""
    records = []
    with open(filename, 'r', encoding="utf-8-sig") as in_file:
        in_file.readline()  # This is to remove the CSV header row
        for line in in_file:  # Where the actual data starts
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()