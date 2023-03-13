from lib.contact_list import *
"""
Initially
ContactList contact_list is an empty list
"""
def test_contact_list_initialise_empty_list():
    contacts = ContactList()
    assert contacts.contact_list == []

"""
Initially
When trying to view a list of contacts, an empty list is returned
"""
def test_view_contacts_initially_returns_an_empty_list():
    contacts = ContactList()
    assert contacts.view_contacts() == []