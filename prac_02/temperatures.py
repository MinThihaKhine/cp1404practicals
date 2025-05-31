"""
Temperature Conversion Program
Min Thiha Khine (#14686570)
"""

#Constant to store menu
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main(): #Main function
    """Display menu and handle temperature conversions until user quits."""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q": # Loops as long as user does not quit (Q)
        if choice == "C": #Convert celsius to fahrenheit
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F": #Convert fahrenheit to celsius
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else: # Invalid option
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)

main() # program starts here

