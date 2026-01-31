from contacts_manager import add_contact, view_contacts, search_contact, delete_contact

def test_add_contact():
    result = add_contact("John", "9876543210", "john@gmail.com")
    assert result == "Contact added successfully"

def test_search_contact():
    contact = search_contact("John")
    assert contact is not None

def test_delete_contact():
    result = delete_contact("John")
    assert result == "Contact deleted successfully"
