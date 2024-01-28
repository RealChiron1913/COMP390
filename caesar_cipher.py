import enchant
import re


def encrypt(message, key, casesensitive=False):  # caesar cipher encrypt
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


def decrypt(encrypted_message, key):  # caesar cipher decrypt with key
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char)
            shifted_code = (char_code - ord('A' if is_upper else 'a') - key) % 26
            decrypted_char = chr(shifted_code + ord('A' if is_upper else 'a'))
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message


def decrypt_without_key(encrypted_message, if_check_words=False):  # caesar cipher decrypt without key
    print('trying to find key...')
    text = encrypted_message.lower()
    counts = {}
    processed = 0
    for letter in text:
        processed += 1
        if processed == int(len(text) / 4):
            print('\r25%', end='')
        elif processed == int(len(text) / 2):
            print('\r50%', end='')
        elif processed == int(len(text) / 4 * 3):
            print('\r75%', end='')
        elif processed == int(len(text)):
            print('\r100%', end='\n')
        if letter.isalpha():
            counts[letter] = counts.get(letter, 0) + 1
    maybe_e = max(counts, key=counts.get)
    password = ord(maybe_e) - ord('e')
    print('key may be: ' + str(password))
    caesar_decrypted_test = caesar_decrypted = decrypt(encrypted_message, password)
    # if if_check_words:
    #     print('current rate is ' + '%.2f' % (check_words(caesar_decrypted_test) * 100) + '%')
    return caesar_decrypted, password


# def check_words(words):  # check if the words are English words
#     print('checking words...')
#     d = enchant.Dict('en_GB')
#     words = re.sub('[^0-9a-zA-Z-]', ' ', words)
#     words = words.split()
#     total = 0
#     checked = 0
#     for word in words:
#         if d.check(word):
#             total += 1
#         checked += 1
#         if int(checked / len(words) * 100) != int((checked - 1) / len(words) * 100):
#             print('\r' + str(int(checked / len(words) * 100)) + '%', end='')
#     print('\r100%', end='\n')
#     rate = total / len(words)
#     return rate
