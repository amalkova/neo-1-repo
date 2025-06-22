#Завдання 4 - бот-помічник

def parse_input(user_input):
    """Парсить введений рядок, повертає команду та аргументи."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    """Додає новий контакт до словника."""
    if len(args) != 2:
        return "Invalid input. Use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Змінює номер телефону існуючого контакту."""
    if len(args) != 2:
        return "Invalid input. Use: change [name] [new_phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    """Повертає номер телефону за ім'ям контакту."""
    if len(args) != 1:
        return "Invalid input. Use: phone [name]"
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    """Виводить усі контакти."""
    if not contacts:
        return "No contacts found."
    result = "Contacts list:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue  # пропускаємо порожній ввід
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

#test_me
#hello
#add John 1234567890
#add Mary 9876543210
#all
#phone John
#phone Mary
#phone Alex
#change John 1111111111
#phone John
#change Alex 2222222222
#add Alex 3333333333
#all
#exit

#add
#add OnlyName
#change
#change John
#change John OnlyPhone
#phone
#phone 
#all
#test
#close