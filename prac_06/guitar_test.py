"""
Estimated: 8 minutes
Actual:  minutes
"""

from prac_06.guitar import Guitar

def main():
    """Test the Guitar class methods."""

    # Create test guitar objects
    gibson = Guitar(name="Gibson L-5 CES", year=1922, cost=16035.40)
    another_guitar = Guitar(name="Another Guitar", year=2013, cost=5000)

def run_test(guitar_object, method_name, expected_result):
    """Test a guitar method and display expected vs actual results."""
    actual_result = getattr(guitar_object, method_name)()
    print(f"{guitar_object.name} {method_name}() - Expected {expected_result}. Got {actual_result}")


