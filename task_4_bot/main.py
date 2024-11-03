import constants
from input_parser import parse_cmd

phone_book = {}

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as err:
            return f"Contact error: {err}"
        except (KeyError, IndexError) as err:
            return f"Unexpected error occurred: {err}"
    return inner

@input_error
def main():
    '''
    The main function which controls the main command processing loop.
    '''   

    print('"How can I help you?\n"')
    print(constants.MENU)
    # Ask user which action he wants to do with a phone_book
    

    # Call parse_input() function to extract desired action from input string using python unpacking
    while True:
        user_input = input('Enter what you wonna do with your phone_book:\n')
        action, args = parse_cmd(user_input)
        # Building a simple match-case statement
        match action:
            case 'add':
                name, phone = args
                print(f"{add_contact(name, phone)}\n")
            case 'change':
                name, phone = args
                print(f"{change_contact(name, phone)}\n")
            case 'phone':
                print(f"{show_phone(args[0])}\n")
            case 'all':
                print(f"{show_all()}\n")
            case 'exit':
                print('Good bye!')
                break
            case _:
                print(f"Command not supported: '{action}', Supported actions are: \n{constants.MENU}");

@input_error
def add_contact(name: str, phone: str) -> str:
    if name in phone_book:
        raise ValueError("contact already exists")
    phone_book[name] = phone
    return "Contact added"


@input_error
def change_contact(name, phone_to_update):
    if name in phone_book:
        phone_book[name] = phone_to_update
        return "Contact updated"
    else:
        raise ValueError("no such contact")

@input_error
def show_phone(name):
    if name in phone_book:
       return phone_book[name]
    else:
        raise ValueError("no such contact")


def show_all():
    return f"All book: {phone_book}"


if __name__ == "main":
    print('hello bot address-book')
    main()

main()
