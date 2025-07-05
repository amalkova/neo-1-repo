from hw10_bot import AddressBook, Record
from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as ve:
            return f"ValueError: {ve}"
        except IndexError:
            return "Not enough arguments provided."
        except Exception as e:
            return f"Error: {e}"
    return inner


def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    return parts[0].lower(), parts[1:]


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    if not record:
        return f"No contact with name '{name}'."
    if record.edit_phone(old_phone, new_phone):
        return "Phone number updated."
    return "Old phone number not found."


@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if not record:
        return f"No contact with name '{name}'."
    if not record.phones:
        return f"No phones found for {name}."
    phones = ", ".join(phone.value for phone in record.phones)
    return f"{name}'s phones: {phones}"


@input_error
def show_all(book: AddressBook):
    if not book.data:
        return "Address book is empty."
    result = ""
    for record in book.data.values():
        result += str(record) + "\n"
    return result.strip()


@input_error
def add_birthday(args, book: AddressBook):
    if len(args) < 2:
        return "Please provide name and birthday (DD.MM.YYYY)."
    name, birthday_str = args[0], args[1]
    record = book.find(name)
    if not record:
        return f"No contact with name '{name}'."
    record.add_birthday(birthday_str)
    return f"Birthday added for {name}."


@input_error
def show_birthday(args, book: AddressBook):
    if not args:
        return "Please provide a contact name."
    name = args[0]
    record = book.find(name)
    if not record:
        return f"No contact with name '{name}'."
    if not record.birthday:
        return f"No birthday set for {name}."
    return f"{name}'s birthday is on {record.birthday}"


@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next 7 days."
    result = "Upcoming birthdays:\n"
    for name, bday in upcoming.items():
        result += f"{name}: {bday}\n"
    return result.strip()


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_phone(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        elif command == "birthdays":
            print(birthdays(args, book))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()