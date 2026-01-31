import json
import os

FILE_NAME = "contacts_data.json"

def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })
    save_contacts(contacts)
    return "Contact added successfully"

def view_contacts():
    return load_contacts()

def search_contact(name):
    contacts = load_contacts()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None

def delete_contact(name):
    contacts = load_contacts()
    updated_contacts = [c for c in contacts if c["name"].lower() != name.lower()]
    save_contacts(updated_contacts)
    return "Contact deleted successfully"
def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            print(add_contact(name, phone, email))

        elif choice == "2":
            contacts = view_contacts()
            for c in contacts:
                print(c)

        elif choice == "3":
            name = input("Enter name to search: ")
            print(search_contact(name))

        elif choice == "4":
            name = input("Enter name to delete: ")
            print(delete_contact(name))

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
