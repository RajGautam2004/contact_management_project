import datetime


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"{self.name} ({self.phone})"

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone


class CallHistory:
    def __init__(self):
        self.call_logs = []

    def log_call(self, contact):
        call_time = datetime.datetime.now()
        self.call_logs.append((contact, call_time))
        print(f"Call to {contact.name} logged at {call_time}.")

    def display_history(self):
        if not self.call_logs:
            print("No call history available.")
        else:
            print("Call History:")
            for contact, time in self.call_logs:
                print(f"Called {contact.name} ({contact.phone}) at {time}")


class ContactManagementSystem:
    def __init__(self):
        self.contacts = []
        self.call_history = CallHistory()

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def delete_contact(self, name):
        contact = self.find_contact_by_name(name)
        if contact:
            self.contacts.remove(contact)
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found.")

    def search_by_letter(self, letter):
        results = [contact for contact in self.contacts if contact.get_name().lower().startswith(letter.lower())]
        if results:
            print(f"Contacts starting with '{letter}':")
            for contact in results:
                print(contact)
        else:
            print(f"No contacts found starting with '{letter}'.")

    def find_contact_by_name(self, name):
        for contact in self.contacts:
            if contact.get_name().lower() == name.lower():
                return contact
        return None

    def call_contact(self, name):
        contact = self.find_contact_by_name(name)
        if contact:
            print(f"Calling {contact.get_name()} at {contact.get_phone()}...")
            self.call_history.log_call(contact)
        else:
            print(f"Contact {name} not found.")

    def display_call_history(self):
        self.call_history.display_history()


class ContactApp:
    def __init__(self):
        self.cms = ContactManagementSystem()

    def run(self):
        while True:
            print("\nAdvanced Contact Management System")
            print("1. Add Contact")
            print("2. Delete Contact")
            print("3. Search by Letter")
            print("4. Call Contact")
            print("5. View Call History")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter contact name: ")
                phone = input("Enter phone number: ")
                self.cms.add_contact(name, phone)
            elif choice == '2':
                name = input("Enter contact name to delete: ")
                self.cms.delete_contact(name)
            elif choice == '3':
                letter = input("Enter the letter to search by: ")
                self.cms.search_by_letter(letter)
            elif choice == '4':
                name = input("Enter contact name to call: ")
                self.cms.call_contact(name)
            elif choice == '5':
                self.cms.display_call_history()
            elif choice == '6':
                print("Exiting the system.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    app = ContactApp()
    app.run()
