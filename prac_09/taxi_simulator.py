""" Min Thiha Khine (#14686570)
CP1404/CP5632 Practical
Taxi Simulator - Step by Step Build
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator program."""
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")


if __name__ == '__main__':
    main()