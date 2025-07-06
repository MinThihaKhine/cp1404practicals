""" MIn Thiha Khine
Estimated: 8 minutes
Actual:  23 minutes
"""

from prac_06.guitar import Guitar

def main():
    """Test the Guitar class methods."""

    # Create test guitar objects
    gibson = Guitar(name="Gibson L-5 CES", year=1922, cost=16035.40)
    another_guitar = Guitar(name="Another Guitar", year=2015, cost=5000)

    # Test get_age() method
    run_test(gibson, "get_age", 103)
    run_test(another_guitar, "get_age", 10)

    # Test is_vintage() method
    run_test(gibson, "is_vintage", True)
    run_test(another_guitar, "is_vintage", False)


def run_test(guitar_object, method_name, expected_result):
    """Test a guitar method and display expected vs actual results."""
    actual_result = getattr(guitar_object, method_name)()
    print(f"{guitar_object.name} {method_name}() - Expected {expected_result}. Got {actual_result}")

if __name__ == "__main__": # So that when imported, it wouldn't show my testings
    main()
