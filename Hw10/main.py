from collections import UserDict


class Field:
    pass


class Name(Field):

    def __init__(self, value):
        self.value = value


class Phone(Field):
    def __init__(self, phone):
        self.value = phone

    def __repr__(self):
        return self.value


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def remove_record(self, record):
        self.data.pop(record.name.value, None)

    def show_records(self):
        return self.data


class Record:
    def __init__(self, new_name, new_phone=None):
        self.name = new_name
        self.phones = []
        if new_phone:
            self.add_phone(new_phone)

    def add_phone(self, new_phone):
        self.phones.append(new_phone)

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones.add_phone(new_phone)
                self.phones.remove_phone(phone)
            else:
                print("Phone number doesn't exist")

    def remove_phone(self, old_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.phones =[]
            else:
                print("Phone number doesn't exist")

    def show_contact(self):
        return {"name": self.name, "phone": self.phones}


if __name__ == '__main__':
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)

    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'

    print('All Ok)')