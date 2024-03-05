

def encrypt(message, key, casesensitive=False):  # substitution cipher encrypt
    # define the alphabets
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    dict_lower = {alphabet_lower[i]: key[i].lower() for i in range(26)}
    dict_upper = {alphabet_upper[i]: key[i].upper() for i in range(26)}

    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if casesensitive is False:
                char = char.upper()
            if char.isupper():
                encrypted_message += dict_upper[char]
            else:
                encrypted_message += dict_lower[char]
        else:
            encrypted_message += char

    return encrypted_message


def decrypt(encrypted_message, key, casesensitive=False):  # substitution cipher decrypt with key
    # define the alphabets
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    dict_lower = {key[i].lower(): alphabet_lower[i] for i in range(26)}
    dict_upper = {key[i].upper(): alphabet_upper[i] for i in range(26)}

    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            if casesensitive is False:
                char = char.upper()
            if char.isupper():
                decrypted_message += dict_upper[char]
            else:
                decrypted_message += dict_lower[char]
        else:
            decrypted_message += char

    return decrypted_message