def parse_input(command):
    parts = command.strip().split()
    return parts[0], parts[1:]

def add_contact(contacts, name, phone):
    contacts[name] = phone
    print("Contact added.")

def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        print("Contact updated.")
    else:
        print("Error: Contact not found.")

def show_phone(contacts, name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Error: Contact not found.")

def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        command = input("Enter a command: ")
        action, args = parse_input(command)
        
        if action in ["close", "exit"]:
            print("Good bye!")
            break
        elif action == "hello":
            print("How can I help you?")
        elif action == "add" and len(args) == 2:
            add_contact(contacts, args[0], args[1])
        elif action == "change" and len(args) == 2:
            change_contact(contacts, args[0], args[1])
        elif action == "phone" and len(args) == 1:
            show_phone(contacts, args[0])
        elif action == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
