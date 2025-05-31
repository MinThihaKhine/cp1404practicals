"""
Min Thiha Khine (#14686570)

Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
#CONSTANTS
VALIDATION_CHECK_NUMBER = 0
LOWER_BOUND_SALES = 1000

LOWER_SALES_BONUS =  0.10
UPPER_SALES_BONUSS = 0.15

sales = float(input("Enter sales: $")) #Get user input

while sales >= VALIDATION_CHECK_NUMBER: #Loop until user enter negative
    if sales < LOWER_BOUND_SALES:  #If sales are under $1,000, the user gets a 10% bonus.
        bonus = sales * LOWER_SALES_BONUS # bonus  calculationn
    else: #If sales are $1,000 or over, the bonus is 15%.
        bonus = sales * UPPER_SALES_BONUSS #bonus calculation

    print(f"Bonus: ${bonus:.2f}") # Output bonus amount in currency format.
    sales = float(input("Enter sales: $")) # Ask sales again to repeat the loop

#Equivalent of my do next thing in the pseudocode
print("Thank you for using this program!") # Just a message to signal that the program is over

