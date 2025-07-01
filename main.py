
from hw06_t01_address_book import AddressBook, Record

def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    print("\n--- Всі записи ---")
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print("\n--- Після редагування телефону John ---")
    print(john)

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"\nJohn: {found_phone}")

    # Видалення запису Jane
    book.delete("Jane")

    print("\n--- Після видалення Jane ---")
    for name, record in book.data.items():
        print(record)

if __name__ == "__main__":
    main()