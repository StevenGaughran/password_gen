import random


def password_generator(characters, upper_letters, the_numbers, the_symbols):
    symbols = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '{', '[', '}', ']', '|',
               ':', ';', '"', "'", '<', ',', '>', '.', '?', '/']

    lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    storage = []

    num_lower_letters = characters - (upper_letters + the_numbers + the_symbols)

    pw_symbols = random.choices(symbols, k=the_symbols)
    for i in pw_symbols:
        storage += i

    pw_numbers = random.choices(numbers, k=the_numbers)
    for i in pw_numbers:
        storage += i

    pw_lower = random.choices(lower_letters, k=num_lower_letters)
    for i in pw_lower:
        storage += i

    pw_upper = random.choices(lower_letters, k=upper_letters)
    upper_upper = [letter.upper() for letter in pw_upper]
    for i in upper_upper:
        storage += i

    random.shuffle(storage)
    password = ''.join(str(e) for e in storage)
    return password
