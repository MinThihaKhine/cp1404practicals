#Menu - Min Thiha Khine (#14686570)

MENU = """(H)ello
(G)oodbye
(Q)uit"""

# Get the user's name
name = input("Enter name: ")

# Display Menu and get first choice
print(MENU)
choice = input(">>> ").upper()

#Conditionals for the menu inside a while loop
while choice != "Q":  #Repeat this block of code unless user enters Q
    if choice == "H": #Prints a hello message
        print("Hello", name)
    elif choice == "G": #Prints a goodbye message
        print("Goodbye", name)
    else:
        print("Invalid choice") #Invalid choice message
    # Display Menu again and get new choice
    print(MENU)
    choice = input(">>> ").upper()

print("Finished.") #Finished message

