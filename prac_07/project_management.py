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

    # Load projects from default file
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()

        if choice == "L":
            filename = input("Filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            print("Filtering projects")
        elif choice == "A":
            print("Adding project")
        elif choice == "U":
            print("Updating project")
        elif choice == "Q":
            save_choice = input(f"Would you like to save to {FILENAME}? ").lower()
            if save_choice.startswith('y'):
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")
        else:
            print("Invalid choice")

def load_projects(filename):
    """Load projects from file and return list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = parts[1]
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def display_projects(projects):
    """Display projects grouped by completion status and sorted by priority."""
    incomplete = []
    complete = []

    for project in projects:
        if project.is_complete():
            complete.append(project)
        else:
            incomplete.append(project)

    # Sort by priority
    incomplete.sort()
    complete.sort()

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in complete:
        print(f"  {project}")

def save_projects(filename, projects):
    """Save projects to file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                      f"{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"{len(projects)} projects saved to {filename}")
if __name__ == "__main__":
    main()