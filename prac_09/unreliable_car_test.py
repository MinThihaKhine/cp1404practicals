"""
CP1404/CP5632 Practical
UnreliableCar Test - Client code to test the UnreliableCar class
"""
from prac_09.unreliable_car import UnreliableCar


def test():
    """Test unreliable car reliability functionality."""
    # Test unreliable car with 40% reliability
    unreliable_car = UnreliableCar("Unreliable", 100, 40)

    # Drive 100 times to test reliability - should drive around 40 times
    for attempt in range(100):
        unreliable_car.drive(1)
    print(unreliable_car)  # Expect odometer to be near 40km



if __name__ == "__main__":
    test()

