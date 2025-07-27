class Band:
    """A band contains multiple musicians."""

    def __init__(self, name):
        """Initialize a band with a name and empty list of musicians."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

