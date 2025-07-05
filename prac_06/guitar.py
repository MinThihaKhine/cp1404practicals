"""
Estimated: 15 minutes
Actual: minutes
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string formatting of the Guitar object"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"



