import random
from keyprocess import process_permutation


def caesar():
    return random.randint(1, 25)

def permutation():
    n = random.randint(1, 9)
    numbers = list(range(1, n + 1))
    user_key = ''.join(map(str, random.sample(numbers, n)))
    return process_permutation(user_key), user_key

def substitution():
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    random.shuffle(alphabet)
    return ''.join(alphabet)