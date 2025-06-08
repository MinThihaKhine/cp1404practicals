import randoms

print(random.randint(5, 20))  # line 1
# What did you see on line 1?
# I saw random integers between 5 and 20
# Smallest number: 5, Largest number: 20


print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2?
# I saw random odd numbers: 3, 5, 7, or 9
# Smallest number: 3, Largest number: 9
# Could line 2 have produced a 4? No, because it starts at 3 with step 2 (odd numbers only)


print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3?
# I saw random floating-point numbers between 2.5 and 5.5
# Smallest number: 2.5, Largest number: 5.5


