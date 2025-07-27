class Band:
    """A band contains multiple musicians."""

    def __init__(self, name):
        """Initialize a band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)


    def __str__(self):
        """Return a string representation of a Band."""
        musician_strings = []
        for musician in self.musicians:
            musician_strings.append(str(musician))
        return f"{self.name} ({', '.join(musician_strings)})"

