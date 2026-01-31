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
