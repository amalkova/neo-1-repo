import pickle

class Person:
    def __init__(self, name, email, phone, favorite=False):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __repr__(self):
        return f"{self.name} ({self.email}, {self.phone})"


class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, person):
        self.contacts.append(person)

    def list_contacts(self):
        for person in self.contacts:
            print(person)