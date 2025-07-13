""" Min Thiha Khine (#14686570)
Estimated time: 40 minutes
Actual time:
"""
from project import Project


FILENAME = "projects.txt"

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def main():
    """Run the project management program."""
    print("Welcome to Pythonic Project Management")
    projects = []

    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()

        if choice == "L":
            print("Loading projects")
        elif choice == "S":
            print("Saving projects")
        elif choice == "D":
            print("Displaying projects")
        elif choice == "F":
            print("Filtering projects")
        elif choice == "A":
            print("Adding project")
        elif choice == "U":
            print("Updating project")
        elif choice == "Q":
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()