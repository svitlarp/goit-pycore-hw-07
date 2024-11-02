from collections import UserDict


class Field():
    # Базовий клас для полів запису.

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)    



class Name(Field):
    #  Клас для зберігання імені контакту.
    pass

name1 = Name('Bob')
name2 = Name('Suizi')
print(name1)
print(name2)


class Phone(Field):
    # Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value   

    @value.setter    
    def value(self, value):
        if not value.isdigit():
            raise TypeError("Phone number should contain digits only, with no other characters")
        if (len(value) != 10):
            raise ValueError("Number should be equal to 10 digits")
        self._value = value 

class Birthday(Field):
    # TODO
    def __init__(self, value):
        try:
            pass
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record():
    # Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        
    def add_birthday(self, date):
        # TODO
        pass    

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)

    def edit_phone(self, phone, new_phone):
        for i in range(len(self.phones)):
            if self.phones[i].value == phone:
                self.phones[i] = Phone(new_phone)

    def find_phone(self, phone):
        return next((p for p in self.phones if p.value == phone), None)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



class AddressBook(UserDict):
    # Клас для зберігання та управління записами.

    def __init__(self):
        self.data = dict()

    def add_record(self, record:Record):                               
        # self.data Реалізовано метод add_record, який додає запис до self.data.
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data[name]

    def delete(self, name: str):
        del self.data[name]


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
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

john_record.remove_phone('5555555555')
print(john)  # Виведення: Contact name: John, phones: 1112223333