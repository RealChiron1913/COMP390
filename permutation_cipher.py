def encrypt(message, key, casesensitive=False):
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


def decrypt(encrypted_message, key, casesensitive=False):
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
    if casesensitive is False:
        decrypted_message = decrypted_message.upper()
    return decrypted_message





