# Contact Book Program

contact_book = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    contact_book[name] = number
    print("Contact added!")

def view_contacts():
    print("Contact Book:")
    for name, number in contact_book.items():
        print(f"{name}: {number}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contact_book:
        print(f"{name}: {contact_book[name]}")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contact_book:
        del contact_book[name]
        print("Contact deleted!")
    else:
        print("Contact not found!")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        break
    else:
        print("Invalid choice! Please try again.")
