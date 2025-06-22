"""
Wimbledon
Estimate: 15 minutes
Actual:   26 minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2

def main():
    """Coordinate the reading, processing and display of Wimbledon data."""
    records = load_records(FILENAME)
    champion_to_count, countries = analyze_data(records)
    display_results(champion_to_count, countries)

def load_records(filename):
    """Read CSV file and return championship data as a list of lists."""
    records = []
    with open(filename, 'r', encoding="utf-8-sig") as in_file:
        in_file.readline()  # This is to remove the CSV header row
        for line in in_file:  # Where the actual data starts
            parts = line.strip().split(",")
            records.append(parts)
    return records

def analyze_data(records):
    """Process records to count champion wins and collect unique countries."""
    champion_to_count = {}
    countries = set()

    for record in records:
        # Add country to set
        country = record[COUNTRY_INDEX]
        countries.add(country)
        # Count championships
        champion = record[CHAMPION_INDEX]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count, countries

def display_results(champion_to_count, countries):
    """Display championship winners and countries."""
    print("Wimbledon Champions: ")
    for champion_name, count in champion_to_count.items():
        print(champion_name, count)
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

main()