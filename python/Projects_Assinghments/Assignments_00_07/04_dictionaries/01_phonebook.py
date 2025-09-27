def read_phone_numbers():
    phonebook = {} 
    print("=== Enter contacts (leave name blank to stop) ===")
    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    print("\n=== Phonebook Entries ===")
    for name in phonebook:
        print(f"{name} -> {phonebook[name]}")


def lookup_numbers(phonebook):
    print("\n=== Lookup Contacts (leave blank to stop) ===")
    while True:
        name = input("Enter name to look up: ")
        if name == "":
            break
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} is not in the phonebook.")


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)
if __name__ == '__main__':
    main()
