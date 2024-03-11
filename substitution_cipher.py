import itertools
from check_words import check_english

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


def decrypt_without_key(encrypted_message, casesensitive):  # substitution cipher decrypt without key
    common_letters = 'etaoinshrdlcumwfgypbvkjxqz'  # Ordered by frequency in English

    for perm in itertools.permutations(common_letters):
        key = ''.join(perm)
        possible_decrypted_message = decrypt(encrypted_message, key, casesensitive)
        
        # Check for common English words or patterns in the decrypted message
        if check_english(possible_decrypted_message):
            return possible_decrypted_message, key
        
    return "Could not decrypt", "Could not decrypt"


def frequency_analysis(encrypted_message):
    # 统计密文中每个单词的出现频率
    encrypted_message = ''.join([char for char in encrypted_message if char.isalpha() or char.isspace()])
    frequency = {}
    for word in encrypted_message.split():
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    # 输出频率最高的前10个单词
            
    print("Frequency Analysis:")
    print("Word\t\tFrequency")
    for word in sorted(frequency, key=frequency.get, reverse=True)[:10]:
        print(word, "\t\t", frequency[word])
