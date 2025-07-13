""" Min Thiha Khine (#14686570)
Estimated time: 20 minutes
Actual time:  minutes
"""

class Project:
    """Represent a project with name, start date, priority, cost estimate, and completion."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return formatted string representation of a Project."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return string representation for debugging."""
        return str(self)
