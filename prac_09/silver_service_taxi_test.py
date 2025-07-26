"""
CP1404/CP5632 Practical
SilverServiceTaxi Test - Client code to test the SilverServiceTaxi class
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def test():
    """Test SilverServiceTaxi functionality."""
    # Test SilverServiceTaxi with fanciness of 2
    silver_service_taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Drive 18km
    silver_service_taxi.drive(18)

    # Check fare calculation
    fare = silver_service_taxi.get_fare()
    print(f"Fare for 18km trip: ${fare:.2f}")
    print(silver_service_taxi)

    # Assert test for the expected fare
    # Calculation: (1.23 * 2 * 18) + 4.50 = 44.28 + 4.50 = 48.78
    assert fare == 48.78, f"Expected $48.78, got ${fare:.2f}"
    print("Test passed! ")


if __name__ == "__main__":
    test()