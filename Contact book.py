class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        """Add a new contact to the contact book."""
        if name in self.contacts:
            print(f"Contact with name '{name}' already exists.")
        else:
            self.contacts[name] = phone
            print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        """Display all contacts."""
        if not self.contacts:
            print("No contacts available.")
        else:
            print("\nContact List:")
            for name, phone in self.contacts.items():
                print(f"Name: {name}, Phone: {phone}")

    def search_contact(self, name):
        """Search for a contact by name."""
        if name in self.contacts:
            print(f"Found: Name: {name}, Phone: {self.contacts[name]}")
        else:
            print(f"No contact found with the name '{name}'.")

    def delete_contact(self, name):
        """Delete a contact by name."""
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' has been deleted.")
        else:
            print(f"No contact found with the name '{name}'.")

    def menu(self):
        """Display the menu for the user."""
        while True:
            print("\nContact Book Menu:")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Search Contact")
            print("4. Delete Contact")
            print("5. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter contact name: ")
                phone = input("Enter contact phone: ")
                self.add_contact(name, phone)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                name = input("Enter contact name to search: ")
                self.search_contact(name)
            elif choice == '4':
                name = input("Enter contact name to delete: ")
                self.delete_contact(name)
            elif choice == '5':
                print("Exiting the Contact Book. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    contact_book = ContactBook()
    contact_book.menu()
