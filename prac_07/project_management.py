""" Min Thiha Khine (#14686570)
Estimated time: 40 minutes
Actual time:
"""
from project import Project, DATE_FORMAT
from datetime import datetime

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

    # CHANGE: Load projects and show count before menu
    try:
        projects = load_projects(FILENAME)
        print(f"Loaded {len(projects)} projects from {FILENAME}")
    except FileNotFoundError:
        print(f"Warning: {FILENAME} not found. Starting with empty project list.")
        projects = []

    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()

        if choice == "L":
            # CHANGE: Added error handling for file loading
            filename = get_valid_string("Filename to load projects from: ")
            try:
                projects = load_projects(filename)
                print(f"Loaded {len(projects)} projects from {filename}")
            except FileNotFoundError:
                print(f"Warning: {filename} not found.")

        elif choice == "S":
            filename = get_valid_string("Filename to save projects to: ")
            save_projects(filename, projects)

        elif choice == "D":
            display_projects(projects)

        elif choice == "F":
            filter_projects_by_date(projects)

        elif choice == "A":
            add_project(projects)

        elif choice == "U":
            # CHANGE: Check if projects exist before updating
            if projects:
                update_project(projects)
            else:
                print("No projects to update!")

        elif choice == "Q":
            # CHANGE: Handle quit with save option - any response not starting with 'n' is yes
            save_choice = input(f"Would you like to save to {FILENAME}? ").lower()
            if not save_choice.startswith('n'):
                save_projects(FILENAME, projects)
            print("Thank you for using custom-built project management software.")

        else:
            print("Invalid choice")


def get_valid_string(prompt):
    """Get non-empty string from user."""
    value = input(prompt).strip()
    while not value:
        print("Input cannot be blank")
        value = input(prompt).strip()
    return value

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


def add_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = get_valid_string("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)


def update_project(projects):
    """Update an existing project's completion and/or priority."""
    # Display all projects with indices
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    choice = int(input("Project choice: "))
    project = projects[choice]
    print(project)

    # Get new values (allow blank to keep existing)
    new_percentage = input("New Percentage: ")
    new_priority = input("New Priority: ")

    if new_percentage:
        project.completion_percentage = int(new_percentage)
    if new_priority:
        project.priority = int(new_priority)


def filter_projects_by_date(projects):
    """Display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    filter_date = datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = []
    for project in projects:
        # Convert project date string to date object for comparison
        project_date = datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if project_date >= filter_date:
            filtered_projects.append(project)

    # Sort by date
    filtered_projects.sort(key=lambda p: datetime.strptime(p.start_date, "%d/%m/%Y"))

    for project in filtered_projects:
        print(project)

if __name__ == "__main__":
    main()