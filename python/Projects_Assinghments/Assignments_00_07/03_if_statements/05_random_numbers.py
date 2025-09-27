import random

def print_random_numbers():
    for _ in range(10):
        number = random.randint(1, 100)
        print(number, end=' ')
    print()  # For a new line after printing all numbers

print_random_numbers()
