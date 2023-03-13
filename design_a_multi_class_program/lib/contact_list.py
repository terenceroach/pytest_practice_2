class ContactList():
    def __init__(self):
        self.contact_list = []
    
    def add(self, contact):
        self.contact_list.append(contact)

    def view_contacts(self):
        numbers_list = []
        for i in self.contact_list:
            print(i.contents)
            numbers_list.append(i.contents)
        return numbers_list