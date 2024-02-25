from itertools import permutations
import enchant


def encrypt(message, key, casesensitive=False):
    columns = len(key)
    rows = (len(message) + columns - 1) // columns
    padding = rows * columns - len(message)
    message += 'X' * padding  # pad the message with 'X' characters

    # if the case is not sensitive, convert the message to uppercase
    if not casesensitive:
        message = message.upper()

    encrypted_chars = []
    for col in key:
        col_index = int(col)
        for row in range(rows):
            # calculate the index of the character in the message
            index = row * columns + col_index
            encrypted_chars.append(message[index])

    # join the encrypted characters to form the encrypted text
    encrypted_text = "".join(encrypted_chars)

    return encrypted_text



def decrypt(encrypted_message, key, casesensitive=False):
    columns = len(key)
    rows = len(encrypted_message) // columns
    
    # if the case is not sensitive, convert the encrypted message to uppercase
    if not casesensitive:
        encrypted_message = encrypted_message.upper()
    
    # initialize a list to store the decrypted characters
    decrypted_chars = []
    
    # iterate through the columns in the key
    for row in range(rows):
        for col in sorted(key, key=lambda x: int(x)):
            index = row + rows * key.index(col)
            decrypted_chars.append(encrypted_message[index])
    
    # join the decrypted characters to form the decrypted message
    decrypted_message = "".join(decrypted_chars)
    
    return decrypted_message



def decrypt_without_key(encrypted_message, casesensitive):
    for columns in range(1, 10):  # assume the key has at most 10 columns
        if len(encrypted_message) % columns == 0:
            for permutation in permutations(range(columns)):
                # decrypt the message using the permutation as the key
                decrypted_message = decrypt(encrypted_message, ''.join(map(str, permutation)), casesensitive)
                if check_english(decrypted_message):
                    # if the decrypted message is in English, return the message and the key
                    key = ''.join([str(p + 1) for p in permutation])
                    return decrypted_message, key
    return "Could not decrypt", "Could not decrypt"


def check_english(text):
    # Initialize an English dictionary
    d = enchant.Dict("en_US")
    
    # Convert text to lowercase and split into words
    words = text.lower().split()
    
    # Determine the number of words to check (up to a threshold of 100)
    threshold = min(100, len(words))
    
    # Use a set for efficient lookup and to remove duplicates within the threshold
    unique_words = set(words[:threshold])
    
    # Count the number of words in the set that are recognized as English
    count = sum(1 for word in unique_words if d.check(word))
    
    # Determine if at least 50% of the words checked are English
    # If the total number of words is less than the threshold, all words are checked
    return count / threshold >= 0.5
