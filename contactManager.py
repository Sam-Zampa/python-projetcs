"""
Contacts list and manager
---
code made in September 2023
"""

#Contacts
class Contacts:
    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email
    
    
#Contacts Manager 
class ContactManager:
    def __init__(self):
        self.contacts = []
    
    #1 add contact
    def add_contact (self, name, number, email):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Contact with the name {name} alredy exist.")
                return
        
        contact = Contacts(name, number, email)
        self.contacts.append(contact)
        print(f"Contact {name} added successfully!")
    
    #2 list contact
    def list_contacts (self):
        for contact in self.contacts:
            print(f"Name: {contact.name} | Number: {contact.number} | E-mail: {contact.email}\n")
    
    #3 search
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(f"Name: {contact.name} | Number: {contact.number} | E-mail: {contact.email}")
                return
        print(f"Contact with the name '{name}' not found.")
        
    
    #4 delete
    def delete_contact (self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact {name} deleted succesfully!")
                return
        print(f"Contact with the name '{name}' not found.")
    
    #5 export
    def export_contacts(self,filename):
        with open(filename,"w") as file:
            for contact in self.contacts:
                file.write(f"Name: {contact.name} | Number: {contact.number} | E-mail: {contact.email}\n")
    
if __name__ == "__main__":
    manager = ContactManager()
        
    while True:
        print("\n Options: ")
        print("1 - Add Contact")
        print("2 - List Contacts")
        print("3 - Search Contact")
        print("4 - Delete Contact")
        print("5 - Export Contacts")
        print("6 - Exit")
        
        option = input("Choose an option: ")
        
        if option == "1":
            name = input("Name: ")
            number = input("Number: ")
            email = input("E-mail: ")
            manager.add_contact(name, number, email)
        elif option == "2":
            manager.list_contacts()
        elif option == "3":
            name = input("Name of the contact to search: ")
            manager.search_contact(name)
        elif option == "4":
            name = input("Name of the contact to delete: ")
            manager.delete_contact(name)
        elif option == "5":
            filename = input("File name to export contacts: ")
            manager.export_contacts(filename)
        elif option == "6":
            break
