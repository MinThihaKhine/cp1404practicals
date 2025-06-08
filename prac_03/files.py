""" files.py
Min Thiha Khine (#14686570)

Make the appropriate choice of file-reading technique for each of these questions:
read()
readline()
readlines()
for line in file
"""

# Question 1: Write user's name to file using open/close
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()
print() # Just for clean output


# Question 2: Read name from file and print greeting using open/close
in_file = open("name.txt", "r")
name_from_file = in_file.read().strip()
in_file.close()
print(f"Hi {name_from_file}!")
print()




# Question 3: Read only first two numbers and add them using with and readline()
with open("numbers.txt", 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
    result = first_number + second_number
print(f"Sum of first two numbers: {result}")
print()

# Question 4: Read all numbers and calculate total using with and for line in file
total = 0
with open("numbers.txt", 'r') as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(f"Total of all numbers: {total}")

