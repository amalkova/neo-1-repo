# Завдання 4 — бот-помічник із декоратором

def input_error(func):
    # Декоратор для обробки помилок у функціях-обробниках команд
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name."
    return inner


def parse_input(user_input):
    # Парсить введений рядок, повертає команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, contacts):
    # Додає новий контакт до словника
    if len(args) != 2:
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts):
    # Змінює номер телефону існуючого контакту
    if len(args) != 2:
        raise ValueError
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args, contacts):
    # Повертає номер телефону за ім'ям контакту
    if len(args) != 1:
        raise IndexError
    name = args[0]
    return contacts[name]  # якщо нема — спрацює KeyError


def show_all(contacts):
    # Виводить усі контакти
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()