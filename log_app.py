from typing import Callable, List, Dict, Tuple


def input_error(func: Callable) -> Callable:
    """
    Декоратор для обробки помилок введення користувача.

    Обробляє винятки KeyError, ValueError, IndexError, що виникають у функціях-обробниках команд.
    """
    def inner(*args, **kwargs) -> str:
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Enter the argument for the command."

    return inner

def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Розбирає введений рядок на команду та аргументи.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Додає новий контакт до словника.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Змінює номер телефону існуючого контакту.
    """
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Показує номер телефону для вказаного контакту.
    """
    name = args[0]
    return contacts[name]

def show_all(contacts: Dict[str, str]) -> str:
    """
    Показує всі збережені контакти.
    """
    if not contacts:
        return "No contacts found."
    
    # Використовуємо списковий вираз для форматування виводу
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main() -> None:
    """
    Головна функція бота-помічника.
    """
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")

    command_handlers = {
        "add": add_contact,
        "change": change_contact,
        "phone": show_phone,
    }

    while True:
        user_input = input("Enter a command: ")
        # Handle empty input
        if not user_input:
            continue
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "all":
            print(show_all(contacts))
        elif command in command_handlers:
            print(command_handlers[command](args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
