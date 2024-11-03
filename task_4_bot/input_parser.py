import re


def parse_cmd(text: str):
    # розбиратиме введений користувачем рядок на команду та її аргументи
    # "add John 1234567890"
    if isinstance(text, str) and text:
        split_input = text.lower().split()
        if re.match(r'^add', text) and len(split_input) == 3:
            return 'add', split_input[1:]
        elif re.match(r'^change', text) and len(split_input) == 3:
            return 'change', split_input[1:]
        elif re.match(r'^phone', text) and len(split_input) == 2:
            return 'phone', split_input[1:]
        elif text.lower() == "all": 
            return 'all', []
        elif text.lower() == "exit":
            return 'exit', []
        else:
            return text, []



# user_input = input('Enter what you wonna do with your phone_book:  ')
# response_action, *given_args = parse_input(user_input)
# print('response action: ', response_action)
# print('given arguments: ', given_args)


# def change_contact(name, phone_to_update):
#     phone_book = {'bob':'9999'}
#     if name in phone_book:
#         phone_book[name] = phone_to_update
#         return "Contact updated."
#     else:
#         raise NameDoestNotExists()


# name, phone = given_args
# print(change_contact(name, phone))

