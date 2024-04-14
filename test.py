import time
import cipher.caesar_cipher as caesar
import cipher.permutation_cipher as permutation
import cipher.substitution_cipher as substitution
import modules.ngram_score as ns


def test_caesar():
    text = "Hello World"
    key = 3
    encrypted = caesar.encrypt(text, key, True)
    if encrypted != "Khoor Zruog":
        return False
    decrypted = caesar.decrypt(encrypted, key)
    if decrypted != text.upper():
        return False
    return True

def test_permutation():
    text = "Hello World"
    key = "3124"
    encrypted = permutation.encrypt(text, key, True)
    if encrypted != "lWdHore lloX":
        return False
    decrypted = permutation.decrypt(encrypted, key)
    if decrypted != "Hello WorldX".upper():
        return False
    return True

def test_substitution():
    text = "Abcdefg Hijklmn opqrstu vwxyz"
    key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    encrypted = substitution.encrypt(text, key, True)
    if encrypted != "Qwertyu Iopasdf ghjklzx cvbnm":
        return False
    decrypted = substitution.decrypt(encrypted, key)
    if decrypted != text.upper():
        return False
    return True

def test_no_key():
    with open("data/hamlet.txt", "r") as file:
        text = file.read()
    caesar_key = 3
    encrypted = caesar.encrypt(text, 3, True)
    if caesar.decrypt_without_key(encrypted) != str(caesar_key):
        return False
    permutation_key = "3124"
    encrypted = permutation.encrypt(text, permutation_key, True)
    if permutation.decrypt_without_key(encrypted) != permutation_key:
        return False
    substitution_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    encrypted = substitution.encrypt(text, substitution_key, True)
    if substitution.decrypt_without_key(encrypted) != substitution_key:
        return False
    return True

if __name__ == '__main__':
    # print(test_caesar())
    # print(test_permutation())
    # print(test_substitution())
    # starttime = time.time()
    # print(test_no_key())
    # endtime = time.time()
    # print(endtime - starttime)

    text = "Looking at the sun without protective equipment such as solar eclipse glasses can harm vision and can lead to serious and permanent damage. Nesheiwat says the sun’s rays can burn the retina and damage the macula, the part of the retina at the back of the eye that is responsible for central vision."
    print(substitution.encrypt(text, "QWERTYUIOPASDFGHJKLZXCVBNM", True))
    



