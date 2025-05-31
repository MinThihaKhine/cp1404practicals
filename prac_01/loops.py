#Min Thiha Khine
#14686570

#Add the following for loop that displays all the odd numbers between 1 and 20 with a space between each one.
ODD_ACCUMULATOR = 0

for i in range(1, 21, 2):
    print(i, end=' ')
    ODD_ACCUMULATOR += i
print()
print("The addition of all the odd numbers between 1 and 20 is : ", ODD_ACCUMULATOR)
print("\n")


# a. Count in 10s from 0 to 100
print("a. Counting in 10s from 0 to 100:") # Output purpose a
for i in range(0, 101, 10):
    print(i, end=' ')
print("\n")  # For neat output

# b. Count down from 20 to 1
print("b. Counting down from 20 to 1:") # Output purpose b
for i in range(20, 0, -1):
    print(i, end=' ')
print("\n") # For neat output


# c. Print n stars based on user input on one line
print("c. Print n stars based on user input on one line:")
number_of_stars = int(input("Number of stars: "))
for star in range(number_of_stars):
    print('*', end='')
print("\n")  # For neat output

# d. Print n lines of increasing stars
print("d. Print n lines of increasing stars:")
# In this scenerio we won't be asking the user for input as the
# number of stars will be using the variable from the program above
for row_of_stars in range(1, number_of_stars + 1):
    print('*' * row_of_stars)
