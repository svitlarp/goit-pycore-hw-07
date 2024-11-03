import re


def parse_cmd(text: str):
    # розбиратиме введений користувачем рядок на команду та її аргументи
    # "add John 1234567890"
    if isinstance(text, str) and text:
        split_input = text.lower().split()
        if re.match(r'^add\s', text) and len(split_input) == 3:
            return 'add', split_input[1:]
        elif re.match(r'^change\s', text) and len(split_input) == 4:
            return 'change', split_input[1:]
        elif re.match(r'^phone\s', text) and len(split_input) == 2:
            return 'phone', split_input[1:]
        elif text.lower() == "all": 
            return 'all', []
        elif re.match(r'^add-birthday', text) and len(split_input) == 3:
            return 'add-birthday', split_input[1:]
        elif re.match(r'^show-birthday', text) and len(split_input) == 2:
            return 'show-birthday', split_input[1]
        elif text == "birthdays":
            return 'birthdays', []
        elif text.lower() == "exit":
            return 'exit', []
        else:
            return text, []


