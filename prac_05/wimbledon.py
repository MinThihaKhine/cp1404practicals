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


    records = []
    with open(FILENAME, 'r', encoding="utf-8-sig") as in_file:
        in_file.readline() # This is to remove the CSV header row
        for line in in_file: # Where the actual data starts
            parts = line.strip().split(",")
            print(parts)
            records.append(parts)
    print(records)




main()