import re
from collections import UserDict
from datetime import datetime
from birthday_function import get_upcoming_birthdays


class Field():
    # Базовий клас для полів запису.

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)    


class Name(Field):
    #  Клас для зберігання імені контакту.
    pass

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
    # Додайте перевірку коректності даних та перетворіть рядок на об'єкт datetime
    def __init__(self, value):
        try:
            # перевірка валідності введеної дати за допомогою бібліотеки datetime
            self.value = datetime.strptime(value, '%d.%m.%Y').date()
        except:
            # юзер френдлі повідомлення про помилку
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record():
    def __init__(self, name):
        self.name = Name(name)
        # TODO Додайте функціонал перевірки на правильність наведених значень для полів Phone, Birthday.
        self.phones = [] 
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
            
    def add_birthday(self, value):
        self.birthday = Birthday(value)

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
        if self.birthday:
            return f'''Contact name: {self.name.value}, 
    phones: {'; '.join(p.value for p in self.phones)}, 
    birthday {self.birthday.value}'''
        else:
            return f'''Contact name: {self.name.value}, 
    phones: {'; '.join(p.value for p in self.phones)}'''

class AddressBook(UserDict):
    # Клас для зберігання та управління записами.

    def __init__(self):
        self.data = dict()
        
    def __str__(self):
        return str(self.data)

    def add_record(self, record:Record):                               
        # self.data Реалізовано метод add_record, який додає запис до self.data.
        self.data[record.name.value] = record

    def find(self, name: str) -> Record:
        return self.data[name]

    def delete(self, name: str):
        del self.data[name]
    
    def get_upcoming_birthdays(self):
        """
        The function should determine list of people whose birthdays are in next 7 days including the current day.
        If the birthday falls on a weekend, the date of the greeting is moved to the following Monday.
        """
        current_date = datetime.today().date()
        
        # Find users whose birthdays are within the next 7 days
        upcoming_birthdays = []
        for username, user in self.data.items():
            # Create birthday for the current year
            if user.birthday:
                current_year_birthday = user.birthday.value.replace(year=current_date.year)
                
                # If the birthday has already passed, skip to next year
                if current_year_birthday < current_date:
                    current_year_birthday = current_year_birthday.replace(year=current_date.year + 1)

                difference = (current_year_birthday - current_date).days

                # Check if the birthday is within the next 7 days
                if 0 <= difference <= 7:
                    # Check if the birthday falls on a weekend (Saturday or Sunday)
                    if current_year_birthday.weekday() in [5, 6]:  # Saturday or Sunday
                        # Move to next Monday
                        next_monday = current_year_birthday + timedelta(days=(7 - current_year_birthday.weekday()))
                        upcoming_birthdays.append({'name': username, 'congratulation_date': str(next_monday)})
                    else:
                        upcoming_birthdays.append({'name': username, 'congratulation_date': str(current_year_birthday)})

        return upcoming_birthdays


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
john_record.add_birthday('6.11.1993')
# john_record.add_birthday('05.04.1997')
# john_record.add_birthday('01.01.1990')
print(john_record)  # To remove

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_birthday('4.12.2002')
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

john_record.remove_phone('5555555555')
print(john)  # Виведення: Contact name: John, phones: 1112223333

print('Address Book: ', book)
print(f"Upcoming birthdays: {book.get_upcoming_birthdays()}")
