from hw12_adress_book import Person
from hw12_storage import save_data, load_data

def main():
    book = load_data()

    while True:
        print("\n1. Додати контакт\n2. Показати контакти\n3. Вийти")
        choice = input("Вибір: ")

        if choice == "1":
            name = input("Ім'я: ")
            email = input("Email: ")
            phone = input("Телефон: ")
            favorite = input("Улюблений контакт? (y/n): ").lower() == "y"
            person = Person(name, email, phone, favorite)
            book.add_contact(person)

        elif choice == "2":
            book.list_contacts()

        elif choice == "3":
            save_data(book)
            print("Адресна книга збережена. Вихід...")
            break

        else:
            print("Невірний вибір!")

if __name__ == "__main__":
    main()