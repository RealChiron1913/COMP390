import itertools
from check_words import check_english
import ngram_score as ns

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


def find_max_letter(message):

    frequency = {}
    for char in message.lower():
        if char.isalpha():
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    # sort the frequency dictionary by the frequency of each character
    frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # return letters only
    sorted_letters = [x[0] for x in frequency]

    return sorted_letters


def find_h(message, e, t):
    message = ''.join([char for char in message if char.isalpha() or char.isspace()])
    frequency = {}
    for word in message.split():
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
            
    for word in sorted(frequency, key=frequency.get, reverse=True):
        if e in word and t in word and len(word) == 3:
            return word[1]

    return None



def get_key(encrypted_message):    
    
    encrypted_message = ''.join([char for char in encrypted_message.lower() if char.isalpha() or char.isspace()])
    common_letters = ''.join([letter for letter in'etaoinshrdlcumwfgypbvkjxqz'])
    frequency = find_max_letter(encrypted_message)
    current_key = {common_letters[i]: frequency[i] for i in range(26)}
    key = Sub_key(current_key)
    key.confirm('e',frequency[0])
    key.confirm('t',frequency[1])
    h = find_h(encrypted_message, key.get_current()['e'], key.get_current()['t'])
    key.confirm('h', h)
    
    print(key.get_unconfirmed())
    print('abcdefghijklmnopqrstuvwxyz')
    print(key.get_formatted())
    fitness_3 = ns.ngram_score('trigrams.txt')
    fitness_4 = ns.ngram_score('quadgrams.txt')
    fitness_words = ns.ngram_score('words.txt')
    while key.get_unconfirmed() != []:
        scores = []
        plain1_list = []
        plain2_list = []
        for letter in key.get_unconfirmed():
            # plain1 = key.get_unconfirmed()[0]
            plain1 = 'r'
            plain2 = letter
            plain1_list.append(plain1)
            plain2_list.append(plain2)
            if plain1 != plain2:
                current_key = key.exchange(plain1, plain2)
            formatted_key = ''.join([current_key[letter] for letter in sorted(current_key)])
            print(formatted_key)
            decrypted_message = decrypt(encrypted_message, formatted_key, True)
            scores = fitness_words.score(decrypted_message)
            print(scores)

        max_score = max(scores)
        max_index = scores.index(max_score)

        print(max_index)
        print(scores)
        print(plain1_list[max_index], plain2_list[max_index])
        break
            


class Sub_key:
    def __init__(self, current_key):
        self.confirmed_key = []
        self.current_key = current_key
        self.unconfirmed_key = [letter for letter in 'etaoinshrdlcumwfgypbvkjxqz']

    def get_plain(self, cipher):
        for plain, c in self.current_key.items():
            if c == cipher:
                return plain

    def confirm(self, plain, cipher):
        current_key = self.current_key
        confirmed_key = self.confirmed_key

        if current_key[plain] != cipher:
            current_key[self.get_plain(cipher)] = current_key[plain]
            current_key[plain] = cipher

        confirmed_key.append(plain)
        self.confirmed_key = confirmed_key
        self.unconfirmed_key.remove(plain)
        self.current_key = current_key
    
    def exchange(self, plain1, plain2):
        current_key = self.current_key.copy()
        cipher1 = current_key[plain1]
        cipher2 = current_key[plain2]

        current_key[plain1], current_key[plain2] = cipher2, cipher1

        return current_key


    def get_unconfirmed(self):
        return self.unconfirmed_key
    
    def get_current(self):
        return self.current_key
    
    def get_confirmed(self):
        return self.confirmed_key
    
    def get_formatted(self):
        # 按字母表顺序输出current_key的值
        return ''.join([self.get_current()[letter] for letter in sorted(self.get_current())])

        # return ''.join([self.get_current()[letter] for letter in self.get_current()])