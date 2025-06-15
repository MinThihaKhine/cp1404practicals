"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    # print(data)
    maximum_subject_length = max(len(entry[0]) for entry in data)
    maximum_teacher_length = max(len(entry[1]) for entry in data)
    maximum_student_length = max(len(str(entry[2])) for entry in data)

    for entry in data:
        subject_code = entry[0]
        teacher_name = entry[1]
        number_of_students = entry[2]
        print(f"{subject_code:<{maximum_subject_length}} is taught by {teacher_name:<{maximum_teacher_length}} and has {number_of_students:>{maximum_student_length}} students")


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append(parts)
        print("----------")
    input_file.close()
    return data


main()