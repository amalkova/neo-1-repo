#################################################################################
#Завдання 1 - caching_fibonacci

from hw05_t01_fibonacci import caching_fibonacci

def main():
    # Отримуємо функцію fibonacci з кешуванням
    fib = caching_fibonacci()

    # Демонстрація роботи функції
    print(f"fib(10) = {fib(10)}")  # 55
    print(f"fib(15) = {fib(15)}")  # 610

if __name__ == "__main__":
    main()


#################################################################################
#Завдання 2 - generator_numbers

from hw05_t02_generator import generator_numbers, sum_profit


def main():
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )

    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income:.2f}")


if __name__ == "__main__":
    main()

#################################################################################
# Завдання 3 - bot_advanced

from hw05_t04_bot_advanced import (
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

# test
# Enter a command: add
# Enter the argument for the command
# Enter a command: add Bob
# Enter the argument for the command
# Enter a command: add Jime 0501234356
# Contact added.
# Enter a command: phone
# Enter the argument for the command
# Enter a command: all
# Jime: 0501234356 
# Enter a command: