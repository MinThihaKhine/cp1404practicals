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
            if projects:
                update_project(projects)
            else:
                print("No projects to update!")

        elif choice == "Q":
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


def get_valid_int(prompt, min_value=None, max_value=None, allow_blank=False):
    """Get valid integer within specified bounds."""
    while True:
        value = input(prompt).strip()

        if allow_blank and value == "":
            return None

        try:
            value = int(value)
            if min_value is not None and value < min_value:
                print(f"Number must be >= {min_value}")
                continue
            if max_value is not None and value > max_value:
                print(f"Number must be <= {max_value}")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_valid_float(prompt, min_value=None):
    """Get valid float number."""
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Number must be >= {min_value}")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_valid_date(prompt):
    """Get valid date in dd/mm/yyyy format."""
    while True:
        date_string = input(prompt).strip()
        try:
            date = datetime.strptime(date_string, DATE_FORMAT)
            return date
        except ValueError:
            print(f"Invalid date format. Please use dd/mm/yyyy")

def load_projects(filename):
    """Load projects from file and return list of Project objects."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            name = parts[0]
            start_date = datetime.strptime(parts[1], DATE_FORMAT)
            priority = int(parts[2])
            cost_estimate = float(parts[3])
            completion_percentage = int(parts[4])
            project = Project(name, start_date, priority, cost_estimate, completion_percentage)
            projects.append(project)
    return projects


def display_projects(projects):
    """Display projects grouped by completion status and sorted by priority."""
    if not projects:
        print("No projects!")
        return

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
            date_str = project.start_date.strftime(DATE_FORMAT)
            file.write(f"{project.name}\t{date_str}\t{project.priority}\t"
                      f"{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"{len(projects)} projects saved to {filename}")


def add_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")

    name = get_valid_string("Name: ")
    start_date = get_valid_date("Start date (dd/mm/yy): ")
    priority = get_valid_int("Priority: ", min_value=1)
    cost_estimate = get_valid_float("Cost estimate: $", min_value=0)
    completion_percentage = get_valid_int("Percent complete: ", min_value=0, max_value=100)

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
    if not projects:
        print("No projects to filter!")
        return

    filter_date = get_valid_date("Show projects that start after date (dd/mm/yy): ")

    filtered_projects = []
    for project in projects:
        if project.is_after_date(filter_date):
            filtered_projects.append(project)

    # Sort by date
    filtered_projects.sort(key=lambda p: p.start_date)

    if filtered_projects:
        for project in filtered_projects:
            print(project)
    else:
        print("No projects found after that date.")

if __name__ == "__main__":
    main()