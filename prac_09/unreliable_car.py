""" Min Thiha Khine (#14686570)
CP1404/CP5632 Practical
UnreliableCar class
"""
import random

from prac_09.car import Car


class UnreliableCar(Car):
    """An unreliable car that only drives based on its reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if random number is less than reliability."""
        MINIMUM_RANDOM_NUMBER = 0
        MAXIMUM_RANDOM_NUMBER = 100
        NO_DISTANCE = 0

        random_number = random.uniform(MINIMUM_RANDOM_NUMBER, MAXIMUM_RANDOM_NUMBER)
        if random_number < self.reliability:
            return super().drive(distance)
        else:
            return NO_DISTANCE