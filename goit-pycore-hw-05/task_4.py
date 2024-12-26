import re

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Error: Contact not found."
        except ValueError:
            return "Error: Invalid input."
        except IndexError:
            return "Error: Missing arguments."
    return wrapper

def parse_input(command):
    parts = command.strip().split()
    return parts[0], parts[1:]

@input_error
def add_contact(contacts, name, phone):
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(contacts, name, phone):
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError

@input_error
def show_phone(contacts, name):
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        raise KeyError

@input_error
def show_all(contacts):
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts found."

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
            print(add_contact(contacts, args[0], args[1]))
        elif action == "change" and len(args) == 2:
            print(change_contact(contacts, args[0], args[1]))
        elif action == "phone" and len(args) == 1:
            print(show_phone(contacts, args[0]))
        elif action == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
    def is_valid_phone(phone):
        pattern = re.compile(r"^\+?\d{10,15}$")
        return pattern.match(phone) is not None

    @input_error
    def add_contact(contacts, name, phone):
        if not is_valid_phone(phone):
            raise ValueError("Invalid phone number format.")
        contacts[name] = phone
        return "Contact added."

    @input_error
    def change_contact(contacts, name, phone):
        if not is_valid_phone(phone):
            raise ValueError("Invalid phone number format.")
        if name in contacts:
            contacts[name] = phone
            return "Contact updated."
        else:
            raise KeyError
