def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(
    args, contacts
):  # тре перевріка на "мало даних", "контакт вже є", "цифри у номері"
    if len(args) < 2:
        return "Not enought data, please try again"
    name, phone = args
    if name in contacts.keys():
        return "The contact is alredy exist, please try another name"
    if not phone.isdigit():
        return "Sorry only numbers accepted to phone, try again"
    contacts[name] = phone
    return "Contact added."


def change_contact(
    args, contacts
):  # тре перевріка на "мало даних", "нема контакту", "нічо не міняється ","цифри у номері"
    if len(args) < 2:
        return "Not enought data, please try again"
    name, phone = args
    if name not in contacts.keys():
        return f"There no {name} in your contacts, please try to add it"
    if not phone.isdigit():
        return "Sorry only numbers accepted to phone, try again"
    if contacts[name] == phone:
        return "There is no changes at phone number"
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):  # тре перевріка на "мало даних", "нема контакту"
    if not args:
        return "Please give name for search"
    name = args[0]
    if name not in contacts.keys():
        return f"There is no {name} in you phone book"
    phone = contacts[name]
    return phone


def get_all(contacts):
    if contacts:
        for name, contact in contacts.items():
            print("Name: {} Phone number: {}".format(name, contact))
    else:
        print("Phone book is empty, you need more friend less code in your life")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            get_all(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
