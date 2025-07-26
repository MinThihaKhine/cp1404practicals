""" Min Thiha Khine # 14686570
CP1404/CP5632 Practical
Taxi Test - Client code to test the Taxi class
"""
from prac_09.taxi import Taxi

# 1. Create a new taxi object, my_taxi, with name "Prius 1", 100 units of fuel and price of $1.23
my_taxi = Taxi("Prius 1", 100, 1.23)

# 2. Drive the taxi 40 km
my_taxi.drive(40)

# 3. Print the taxi's details and the current fare
print(my_taxi)
print(f"Current fare: ${my_taxi.get_fare():.2f}")


