"""
Shop Calculator

Min Thiha Khine
#14686570
"""

#CONSTANTS
VALIDATION_CHECK_NUMBER = 0
DISCOUNT_RATE = 0.10
DISCOUNT_SALES_THRESHOLD = 100

#Accuumulator
total_price = 0

number_of_items = int(input("Number of items: ")) #User input for number of items

#Validation check for number of items
while number_of_items < VALIDATION_CHECK_NUMBER:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Ask for each item price based on user input(number_of_items)
for each_item in range(number_of_items):
    each_item_price = float(input("Price of item: "))
    while each_item_price <= VALIDATION_CHECK_NUMBER:
        print("Invalid price!")
        each_item_price = float(input("Price of item: "))
    total_price += each_item_price #accumulate total price

# Apply Discount if total amount exceeds 100
if total_price > DISCOUNT_SALES_THRESHOLD:
    discount_amount = total_price * DISCOUNT_RATE
    final_price = total_price - discount_amount

print(f"Total price for {number_of_items} items is ${total_price:.2f}") #Final output with currency format
