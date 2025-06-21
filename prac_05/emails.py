"""
Email
Estimate: 15 minutes
Actual:   16 minutes
"""

def main():
    """Main program"""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        choice = input(f"Is your name {name}? (Y/n) ").lower().strip()
        if not (choice == "y" or choice == ""):
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    name = " ".join(email.split("@")[0].split('.'))
    return name.title()

main()
