from pycipher import SimpleSubstitution as SimpleSub
import random
import re
from ngram_score import ngram_score
from check_words import check_english
fitness = ngram_score('quadgrams.txt') # load our quadgram statistics

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
    key = find_key(encrypted_message)

    return decrypt(encrypted_message, key, casesensitive), key



def find_key(encrypted_message, maxlen=3000):
    length = min(maxlen, len(encrypted_message))
    encrypted_message = encrypted_message[:length]
    maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    maxscore = -99e9
    parentscore, parentkey = maxscore, maxkey[:]

    ctext = re.sub('[^A-Z]', '', encrypted_message.upper())
    i = 0
    detext = decrypt(encrypted_message, maxkey)

    while not check_english(detext):
        i = i + 1
        random.shuffle(parentkey)
        deciphered = SimpleSub(parentkey).decipher(ctext)
        parentscore = fitness.score(deciphered)
        count = 0
        while count < 1000:
            a = random.randint(0, 25)
            b = random.randint(0, 25)
            child = parentkey[:]
            child[a], child[b] = child[b], child[a]
            deciphered = SimpleSub(child).decipher(ctext)
            score = fitness.score(deciphered)
            if score > parentscore:
                parentscore = score
                parentkey = child[:]
                count = 0
            count = count + 1
        if parentscore > maxscore:
            maxscore, maxkey = parentscore, parentkey[:]
            print('\nbest score so far:', maxscore, 'on iteration', i)
            print('    best key: ' + ''.join(maxkey))
            detext = decrypt(encrypted_message, maxkey)


    return ''.join(maxkey)


    
    


