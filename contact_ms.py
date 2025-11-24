import json
import os

class ContactManager:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()
    


    def load_contacts(self):
        """if the file exists, load contacts"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.contacts = json.load(file)
                print(f"Loaded {len(self.contacts)} contacts.")
            except Exception as e:
                print(f"Error loading contacts: {e}")
                self.contacts = []
        else:
            self.contacts = []
    


    def save_contacts(self):
        """save contacts to file"""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.contacts, file, indent=2)
            print("Contacts saved successfully!")
        except Exception as e:
            print(f"Error saving contacts: {e}")
    


    def add_contacts(self):
        """add a new contact"""
        print("\n---Add New Contact---")
        name = input("Enter Name: ").strip()
        phone = input("Enter Phone: ").strip()
        email = input("Enter Email: ").strip()

        # validate name
        if not name:
            print("Error: Name cannot be empty")
            return
        
        # create dictionary
        contact = {
            "name": name,
            "phone": phone, 
            "email": email
        }

        self.contacts.append(contact)
        self.save_contacts()
        print(f"Contact '{name}' added successfully!")



    
    def view_contacts(self):
        """list all the contacts"""
        print("\n---All Contacts---")

        if not self.contacts:
            print("Oooops! No Contacts Found.")
            return 
        
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index} | Name: {contact['name']}")
            print(f"    Phone: {contact['phone']}")
            print(f"    Email: {contact['email']}")
    



    def search_contact(self):
        """search by name"""
        if not self.contacts:
            print("No contacts to search.")
            return
        
        search_term = input("Enter name to search for: ").strip().lower()
        if not search_term:
            print("Please enter a search term.")
            return
        
        found_contacts = []
        for contact in self.contacts:
            if search_term in contact['name'].lower():
                found_contacts.append(contact)
        
        if found_contacts:
            print(f"\n--- Found {len(found_contacts)} matching contacts ---")
            for index, contact in enumerate(found_contacts, start=1):
                print(f"{index}. Name: {contact['name']}")
                print(f"   Phone: {contact['phone']}")
                print(f"   Email: {contact['email']}")
                print()
        else:
            print("No contacts found matching your search.")



    def delete_contacts(self):
        """delete by position"""
        self.view_contacts()  # Show contacts first
        
        if not self.contacts:
            return  
        
        try:
            contact_num = int(input("Enter the number of contact to delete: "))
            if 1 <= contact_num <= len(self.contacts):
                deleted_contact = self.contacts.pop(contact_num - 1)
                self.save_contacts()  # Save after deletion
                print(f"Deleted contact: '{deleted_contact['name']}'")
            else:
                print("Invalid contact number!")
        except ValueError:
            print("Please enter a valid number!")



    def run(self):
        """main app loop"""
        while True:
            print("\n=== Contact Manager ===")
            print("1. Add Contact")
            print("2. View All Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Exit")

            choice = input("Enter your choice(1-5): ").strip()
            if choice == "1":
                self.add_contacts()
            elif choice == "2":
                self.view_contacts()
            elif choice == "3":
                self.search_contact()
            elif choice == "4":
                self.delete_contacts()
            elif choice == "5":
                self.save_contacts()
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")
        
if __name__ == "__main__":
    app = ContactManager()
    app.run()
