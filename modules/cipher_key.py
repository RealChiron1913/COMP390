import random
import re


class key():
    def __init__(self, key=None, method=None):
        self.key = key
        self.method = method
        self.message = None

    def get(self):
        return self.key

    def check(self, method):
        key = self.key
        if key is None:
            return False
        if method == 'caesar':
            if key.isdigit():
                return True
        if method == 'permutation':
            if len(key) > 9:
                return False
            if not key.isdigit():
                return False
            if len(set(key)) != len(key):
                return False
            return True
        if method == 'substitution':
            if len(key) != 26:
                return False
            if not key.isalpha():
                return False
            if len(set(key)) != len(key):
                return False
            return True
        return False
    
    def randomkey(self):
        method = self.method
        if method == 'caesar':
            self.key = str(random.randint(1, 25))
            return self.key
        if method == 'permutation':
            n = random.randint(1, 9)
            numbers = list(range(1, n + 1))
            self.key = ''.join(map(str, random.sample(numbers, n)))
            return self.key
        if method == 'substitution':
            alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            random.shuffle(alphabet)
            self.key = ''.join(alphabet)
            return self.key
    
    def process(self, keyprocess):
        if keyprocess:
            self.key = key_process(self.key, self.method)
        return self.key
       
        

def remove_duplicates(number_strings):
    appeared = set()
    unique = []
    for number in number_strings:
        if number not in appeared:
            unique.append(number)
            appeared.add(number)
    return unique

def sort_and_index(number_strings):
    numbers = [int(s) for s in number_strings]
    sorted_numbers = sorted(numbers)
    processed = []
    for number in number_strings:
        index = sorted_numbers.index(int(number))
        processed.append(index)
    return processed

def key_process(number_strings, method):
    
    if method=='substitution':
        number_strings = remove_duplicates(number_strings.upper())
        number_strings = [char for char in number_strings if char.isalpha()]
        alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        random.shuffle(alphabet)
        for char in alphabet:
            if char not in number_strings:
                number_strings.append(char)
        number_strings = ''.join(number_strings)
        return number_strings

    if number_strings == '':
        return ''
    
    number_strings = ''.join([str(ord(char)) if not char.isdigit() else char for char in number_strings])
    number_strings = str(round(float(number_strings))*round(float(number_strings))*len(number_strings))

    if method=='caesar':
        return number_strings
    
    elif method=='permutation':
        number_strings = remove_duplicates(number_strings)
        processed = sort_and_index(number_strings)
        processed = ''.join([str(int(i)+1) for i in processed])
        return processed
    
