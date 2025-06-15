""" lists_warm_up.py
Min Thiha Khine
14686570
"""
numbers = [3, 1, 4, 1, 5, 9, 2]

# Predicted values for expressions:
# numbers[0] = 3 (first element)
# numbers[-1] = 2 (last element)
# numbers[3] = 1 (fourth element, index 3)
# numbers[:-1] = [3, 1, 4, 1, 5, 9] (all elements except the last)
# numbers[3:4] = [1] (from index 3 to 4 but not including 4)
# 5 in numbers = True
# 7 in numbers = False
# "3" in numbers = False (string "3" is not in the list, only integer 3)
# numbers + [6, 5, 3] = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] (concatenated lists)


# In the same Python file, write statements to achieve the following:
print(f"original list: {numbers} \n")

# 1. Change the first element of numbers to "ten" (the string, not the number 10)
numbers[0] = "ten"
print(f"After changing first element to 'ten':  {numbers} \n")

# 2. Change the last element of numbers to 1
numbers[-1] = 1
print(f"After changing last element to 1:  {numbers} \n")

# 3. Print all the elements from numbers except the first two (slice)
print(f"All elements except first two: {numbers[2:]} \n")

# 4. Print whether 9 is an element of numbers
print(f"Is 9 an element of numbers? {9 in numbers}")