

def encrypt(message, key, casesensitive=False):
    key = key_process(key)
    columns = len(key)
    rows = (len(message) + columns - 1) // columns
    padding = rows * columns - len(message)
    message += 'X' * padding
    matrix = [list(message[i:i + columns]) for i in range(0, len(message), columns)]
    encrypted_text = ""
    for col in key:
        col_index = int(col)
        for row in range(rows):
            encrypted_text += matrix[row][col_index]
    if casesensitive is False:
        encrypted_text = encrypted_text.upper()
    return encrypted_text


def decrypt(encrypted_message, key):
    key = key_process(key)
    columns = len(key)
    rows = len(encrypted_message) // columns
    matrix = [['' for _ in range(columns)] for _ in range(rows)]
    index = 0
    for col in key:
        col_index = int(col)
        for row in range(rows):
            matrix[row][col_index] = encrypted_message[index]
            index += 1

    decrypted_message = ""
    for row in matrix:
        decrypted_message += "".join(row)

    return decrypted_message

def key_process(number_strings):
    number_strings = ''.join([str(ord(char)) if char.isalpha() else char for char in number_strings])
    number_strings = str(int(number_strings)*int(number_strings)*len(number_strings))
    print(number_strings)
    appeared = set()
    unique = []
    for number in number_strings:
        if number not in appeared:
            unique.append(number)
            appeared.add(number)
    number_strings = unique
    numbers = [int(s) for s in number_strings]
    sorted_numbers = sorted(numbers)
    processed = []
    for number in number_strings:
        index = sorted_numbers.index(int(number))
        processed.append(index)
    print(processed)
    # to int
    processed = ''.join([str(i) for i in processed])
    return processed

def key_process(number_strings):
    number_strings = ''.join([str(ord(char)) if char.isalpha() else char for char in number_strings])
    number_strings = str(int(number_strings)*int(number_strings)*len(number_strings))
    print(number_strings)
    appeared = set()
    unique = []
    for number in number_strings:
        if number not in appeared:
            unique.append(number)
            appeared.add(number)
    number_strings = unique
    numbers = [int(s) for s in number_strings]
    sorted_numbers = sorted(numbers)
    processed = []
    for number in number_strings:
        index = sorted_numbers.index(int(number))
        processed.append(index)
    print(processed)
    # to int
    processed = ''.join([str(i) for i in processed])
    return processed



