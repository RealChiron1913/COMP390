from itertools import permutations
import enchant


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


def decrypt_without_key(encrypted_message, casesensitive):
    for columns in range(1, 10):
        if len(encrypted_message) % columns == 0:
            for permutation in permutations(range(columns)):
                key = "".join(str(i) for i in permutation)
                print(key)
                decrypted_message = decrypt(encrypted_message, key, casesensitive)
                if check_english(decrypted_message):
                    return decrypted_message, key
    return "Could not decrypt", "Could not decrypt"     # if the key is not found


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
    
    # Print the count and the threshold for debugging purposes
    print(count, threshold)
    
    # Determine if at least 50% of the words checked are English
    # If the total number of words is less than the threshold, all words are checked
    return count / threshold >= 0.5
