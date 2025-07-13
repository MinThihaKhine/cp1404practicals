""" Min Thiha Khine (#14686570)
Estimated time: 20 minutes
Actual time:  21 minutes
"""
from datetime import datetime

DATE_FORMAT = "%d/%m/%Y"

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
        """Return string representation of a Project."""
        # Format date string if it's not already formatted
        if '/' in self.start_date and len(self.start_date.split('/')[2]) == 4:
            # Convert to date object and format
            date_obj = datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()
            date_str = date_obj.strftime("%d/%m/%Y")
        else:
            date_str = self.start_date

        return (f"{self.name}, start: {date_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __repr__(self):
        """Return string representation for debugging."""
        return str(self)

    def __lt__(self, other):
        """Compare projects by priority for sorting."""
        return self.priority < other.priority

    def is_complete(self):
        """Determine if the project is complete."""
        return self.completion_percentage == 100

    def is_after_date(self, date):
        """Check if project starts after or on the given date."""
        return self.start_date >= date

