#Тема 6
#################################################################################
#Завдання 1 - total_salary(path) = загальна та середня сума заробітної плати

from hw04_t01_salary import create_test_salary_file, total_salary

def main():
    create_test_salary_file()
    print("Файл salary_file.txt успішно створено.")

    total, average = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()

#################################################################################
#Завдання 2 - get_cats_info(path) = список словників з інформацією про кожного кота
from hw04_t02_cat import create_test_cats_file, get_cats_info

def main():
    create_test_cats_file()

    cats_info = get_cats_info("cats_file.txt")

    print("\nРезультат виконання get_cats_info:")
    for cat in cats_info:
        print(cat)

if __name__ == "__main__":
    main()

#################################################################################
#Завдання 3 - структура папок

#Використовуйте модуль sys для отримання шляху до директорії як аргументу командного рядка.
import sys
from pathlib import Path
from colorama import Fore
from hw04_t03_folder import print_directory_structure, validate_directory_path

#Забезпечте належне форматування виводу, використовуючи функції colorama.

def main():
    # Якщо немає аргументу — попросити ввести шлях через input()
    if len(sys.argv) == 2:
        directory_path = Path(sys.argv[1])
    else:
        print(f"{Fore.YELLOW}Не вказано шлях до директорії як аргумент командного рядка.")
        user_input = input(f"{Fore.CYAN}Введіть повний шлях до директорії: ")
        directory_path = Path(user_input.strip())
    try:
        validate_directory_path(directory_path)
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"{Fore.RED}Помилка: {e}")
        sys.exit(1)

    print(f"{Fore.YELLOW}📂 Структура директорії: {directory_path}\n")
    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()

#################################################################################
#Завдання 4 - бот-помічник
from hw04_t04_bot import (
    parse_input,
    add_contact,
    change_contact,
    show_phone,
    show_all
)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input:
            continue
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