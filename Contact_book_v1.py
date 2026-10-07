contacts = []

def Add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    if not name:
        print("Name cannot be empty.")
        return
    if not phone:
        print("Phone number cannot be empty.")
        return
    if not email:
        print("Email cannot be empty.")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print("Contact Added Successfully.")

def View_contact():
    if not contacts:
        print("No contacts available.")
        return
    for number, contact in enumerate(contacts, start=1):
        print(number,contact)

def Search_contact():
    phone = input("Enter phone number: ")

    for contact in contacts:
        if contact["phone"] == phone:
            print(contact)
            return
    print("Contact not found.")

def Update_contact():
    phone = input("Enter phone number: ")

    for contact in contacts:
        if contact["phone"] == phone:
            new_name = input("Enter new name: ")
            contact["name"] = new_name
            print("Name updated successfully.")
            new_phone = input("Enter new Phone: ")
            contact['phone'] = new_phone
            print("Phone updated successfully.")
            new_email = input("Enter new email: ")
            contact["email"] = new_email
            print("Email updated successfully.")
            return
    print("Contact not found")

def Delete_contact():
    phone = input("Enter phone number: ")

    for contact in contacts:
        if contact["phone"] == phone:
            confirmation = input("Are you sure: y/n: ").lower()
            if confirmation == "y":
                contacts.remove(contact)
                print("Contact deleted successfully.")
                return
            elif confirmation == 'n':
                print("Cancelled.")
                return
            else:
                print("Enter y or n. ")
    print("Contact not found")

def menu():
    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    return choice

while True:
    choice = menu()

    if choice == 1:
        Add_contact()

    elif choice == 2:
        View_contact()

    elif choice == 3:
        Search_contact()
    elif choice == 4:
        Update_contact()
    elif choice == 5:
        Delete_contact()
    elif choice == 6:
        print("Exiting the Program...\nThankyou......")
        break
    else:
        print("Enter a valid input")