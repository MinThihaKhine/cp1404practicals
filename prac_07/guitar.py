"""Min Thiha Khine
Estimated: 15 minutes
Actual: 12 minutes
"""

from datetime import datetime

VINTAGE_AGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        """Initialize a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string formatting of the Guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Return True if this guitar's year is less than other guitar's year."""
        return self.year < other.year

    def get_age(self):
        """Return the age of the guitar in years."""
        current_year  = datetime.today().year
        age = current_year - self.year
        return age

    def is_vintage(self):
        """Return True if guitar age is 50 or more years old, False otherwise."""
        return self.get_age() >= VINTAGE_AGE

