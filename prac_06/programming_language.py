"""
Estimated: 8 minutes
Actual:
"""

class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage object"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of the ProgrammingLanguage object"""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return whether the class typing is Dynamic or not."""
        return self.typing == "Dynamic"