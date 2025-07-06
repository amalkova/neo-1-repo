import unittest
from io import StringIO
import sys
from hw10_bot import AddressBook, Record
from hw10 import add_contact, change_phone, show_phone, show_all, add_birthday, show_birthday, birthdays


class TestAddressBookBot(unittest.TestCase):

    def setUp(self):
        self.book = AddressBook()

    def test_add_contact_new_and_update(self):
        # Додаємо новий контакт
        result = add_contact(["Alice", "1234567890"], self.book)
        self.assertEqual(result, "Contact added.")
        self.assertIn("Alice", self.book.data)
        self.assertEqual(len(self.book.find("Alice").phones), 1)

        # Додаємо ще один телефон до існуючого
        result = add_contact(["Alice", "0987654321"], self.book)
        self.assertEqual(result, "Contact updated.")
        self.assertEqual(len(self.book.find("Alice").phones), 2)

    def test_add_contact_invalid_phone(self):
        result = add_contact(["Bob", "abc123"], self.book)
        self.assertTrue("ValueError" in result)

    def test_change_phone_success_and_fail(self):
        add_contact(["Carol", "1234567890"], self.book)
        result = change_phone(["Carol", "1234567890", "1111111111"], self.book)
        self.assertEqual(result, "Phone number updated.")
        # Невдалий пошук старого номера
        result = change_phone(["Carol", "2222222222", "3333333333"], self.book)
        self.assertEqual(result, "Old phone number not found.")

    def test_show_phone(self):
        add_contact(["Dave", "1234567890"], self.book)
        add_contact(["Dave", "2222222222"], self.book)
        result = show_phone(["Dave"], self.book)
        self.assertIn("1234567890", result)
        self.assertIn("2222222222", result)

    def test_show_phone_no_contact(self):
        result = show_phone(["NonExist"], self.book)
        self.assertIn("No contact", result)

    def test_show_all_empty_and_nonempty(self):
        result = show_all(self.book)
        self.assertEqual(result, "Address book is empty.")
        add_contact(["Eve", "1234567890"], self.book)
        result = show_all(self.book)
        self.assertIn("Eve", result)
        self.assertIn("1234567890", result)

    def test_add_birthday_and_show(self):
        add_contact(["Frank", "1234567890"], self.book)
        result = add_birthday(["Frank", "01.01.2000"], self.book)
        self.assertEqual(result, "Birthday added for Frank.")
        result = show_birthday(["Frank"], self.book)
        self.assertIn("01.01.2000", result)

    def test_add_birthday_invalid_format(self):
        add_contact(["Grace", "1234567890"], self.book)
        result = add_birthday(["Grace", "2000-01-01"], self.book)
        self.assertTrue("ValueError" in result)

    def test_show_birthday_no_birthday(self):
        add_contact(["Hank", "1234567890"], self.book)
        result = show_birthday(["Hank"], self.book)
        self.assertIn("No birthday set", result)

    def test_birthdays_upcoming(self):
        add_contact(["Ivy", "1234567890"], self.book)
        # Встановимо день народження через 3 дні від сьогодні
        from datetime import datetime, timedelta
        future_date = (datetime.now() + timedelta(days=3)).strftime("%d.%m.%Y")
        add_birthday(["Ivy", future_date], self.book)
        result = birthdays([], self.book)
        self.assertIn("Ivy", result)

    def test_birthdays_no_upcoming(self):
        result = birthdays([], self.book)
        self.assertIn("No birthdays", result)

    def test_validation_phone_too_short(self):
        result = add_contact(["Jack", "12345"], self.book)
        self.assertTrue("ValueError" in result)

    def test_validation_phone_too_long(self):
        result = add_contact(["Jack", "1234567890123"], self.book)
        self.assertTrue("ValueError" in result)

    def test_program_exit(self):
        # Тестування коректного виходу з програми в інтеграційному тесті
        import builtins

        inputs = iter([
            "hello",
            "add John 1234567890",
            "phone John",
            "add-birthday John 01.01.1990",
            "show-birthday John",
            "birthdays",
            "all",
            "exit"
        ])

        outputs = []

        def fake_input(prompt):
            return next(inputs)

        def fake_print(*args, **kwargs):
            outputs.append(" ".join(str(a) for a in args))

        # Збережемо оригінальні функції
        orig_input = builtins.input
        orig_print = builtins.print

        try:
            builtins.input = fake_input
            builtins.print = fake_print
            import hw10
            hw10.main()
        finally:
            builtins.input = orig_input
            builtins.print = orig_print

        # Перевірка що виведено "Good bye!" при команді exit
        self.assertTrue(any("Good bye!" in line for line in outputs))


if __name__ == "__main__":
    unittest.main()