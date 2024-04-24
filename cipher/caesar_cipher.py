
def encrypt(message, key, casesensitive=False):  # caesar cipher encrypt
    key = int(key)
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if casesensitive is False:
                char = char.upper()
            is_upper = char.isupper()
            char_code = ord(char)
            shifted_code = (char_code - ord('A' if is_upper else 'a') + key) % 26
            encrypted_char = chr(shifted_code + ord('A' if is_upper else 'a'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(encrypted_message, key, casesensitive=False):# caesar cipher decrypt with key
    key = int(key)
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            if casesensitive is False:
                char = char.upper()
            is_upper = char.isupper()
            char_code = ord(char)
            shifted_code = (char_code - ord('A' if is_upper else 'a') - key) % 26
            decrypted_char = chr(shifted_code + ord('A' if is_upper else 'a'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message


def decrypt_without_key(encrypted_message):  # caesar cipher decrypt without key
    dict = {}
    for i in encrypted_message:
        if i.isalpha():
            i = i.upper()
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
    
    max_value = max(dict.values())
    for key, value in dict.items():
        if value == max_value:
            most_common_letter = key
            break

    key = ord(most_common_letter) - ord('E')
    return str(key)

