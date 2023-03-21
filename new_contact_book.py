# Initialize an empty dictionary to store contacts
contacts = {}

# Define a function to add a new contact to the dictionary
def add_contact():
    # Prompt the user to enter the contact's name, phone number, and email address
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    # Add the contact's name and phone number to the contacts dictionary
    contacts[name] = phone
    # Print a message to confirm that the contact has been added
    print(f"{name} added to contacts.")

# Define a function to retrieve a contact's phone number by name
def get_contact_phone():
    # Prompt the user to enter the contact's name
    name = input("Enter name to search for: ")
    # If the contact's name is in the contacts dictionary,
    if name in contacts:
        # Return the contact's phone number
        return contacts[name]
    else:
        # Otherwise, return None
        return None

# Define a function to update a contact's phone number by name
def update_contact_phone():
    # Prompt the user to enter the contact's name and new phone number
    name = input("Enter name to update: ")
    phone = input("Enter new phone number: ")
    # If the contact's name is in the contacts dictionary,
    if name in contacts:
        # Update the contact's phone number in the contacts dictionary
        contacts[name] = phone
        # Print a message to confirm that the contact's phone number has been updated
        print(f"{name}'s phone number updated.")
    else:
        # Otherwise, print a message indicating that the contact was not found in the dictionary
        print(f"{name} not found in contacts.")

# Define a function to remove a contact from the contacts dictionary by name
def delete_contact():
    # Prompt the user to enter the contact's name
    name = input("Enter name to delete: ")
    # If the contact's name is in the contacts dictionary,
    if name in contacts:
        # Remove the contact from the contacts dictionary
        del contacts[name]
        # Print a message to confirm that the contact has been deleted
        print(f"{name} deleted from contacts.")
    else:
        # Otherwise, print a message indicating that the contact was not found in the dictionary
        print(f"{name} not found in contacts.")

# Define a function to list all contacts by name
def list_contacts():
    # Print a message indicating that the following list shows all contacts
    print("Contacts:")
    # For each contact's name in the contacts dictionary,
    for name in contacts:
        # Print the contact's name and phone number
        print(f"{name}: {contacts[name]}")

# Define a function to display the menu of options
def display_menu():
    # Print a menu of options for the user to choose from
    print("""
    1. Add a contact
    2. Find a contact by name
    3. Update a contact's phone number by name
    4. Remove a contact by name
    5. List all contacts
    6. Exit
    """)

# Display the menu of options
display_menu()

# Loop until the user chooses to exit
while True:
    # Prompt the user to choose an option from the menu
    choice = input("Enter your choice: ")
    # If the user chooses to add a contact,
    if choice == "1":
        add_contact()
    # If the user chooses to find a contact by name,
    elif choice == "2":
        # Call the function to retrieve a contact's phone number by name
        phone = get_contact_phone()
        # If the contact's phone number was found in the contacts dictionary,
        if phone is not None:
            # Print the contact's name and phone number
            print(f"Phone number for {name}: {phone}")
        else:
            # Otherwise, print a message indicating that the contact was not found in the dictionary
            print(f"{name} not found in contacts.")
    # If the user chooses to update a contact's phone number by name,
    elif choice == "3":
        # Call the function to update a contact's phone number by name
        update_contact_phone()
    # If the user chooses to remove a contact by name,
    elif choice == "4":
        # Call the function to remove a contact from the contacts dictionary by name
        delete_contact()
    # If the user chooses to list all contacts,
    elif choice == "5":
        # Call the function to list all contacts by name
        list_contacts()
    # If the user chooses to exit,
    elif choice == "6":
        # Print a message indicating that the program is exiting
        print("Exiting program.")
        # Break out of the loop to exit the program
        break
    # If the user enters an invalid choice,
    else:
        # Print a message indicating that the choice was invalid
        print("Invalid choice. Please try again.")
    # Display the menu of options again
    display_menu()


