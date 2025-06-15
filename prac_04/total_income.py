"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    number_of_months = int(input("How many months? "))
    print()
    incomes = get_incomes(number_of_months) # Extra refactoring for clean code
    print_report(incomes, number_of_months)

def get_incomes(number_of_months):
    """Get a list of all incomes for a given number of months."""
    incomes = []
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))  # Refactored to use f string
        incomes.append(income)
    return incomes

def print_report(incomes, number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

main()
