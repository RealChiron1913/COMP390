import random
from keyprocess import key_process


def caesar():
    return random.randint(1, 25)

def permutation():
    n = random.randint(1, 9)
    numbers = list(range(1, n + 1))
    user_key = ''.join(map(str, random.sample(numbers, n)))
    return key_process(user_key, 'permutation', False), user_key