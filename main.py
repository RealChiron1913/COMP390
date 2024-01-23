import caesar_cipher as caesar
import permutation_cipher as permutation


def gettext(path="hamlet.txt"):  # get text from file
    text = open(path, "r").read()
    return text


def encrypt(text, method, key=0, allupper=True):  # encrypt text
    if method == 'caesar':
        return caesar.encrypt(text, key, allupper)
    if method == 'permutation':
        return permutation.encrypt(text, key, allupper)


def decrypt(text, method, key=0):  # decrypt text
    if method == 'caesar':
        return caesar.decrypt(text, key)
    if method == 'permutation':
        return permutation.decrypt(text, key)


if __name__ == '__main__':

    # caesar cipher
    # encrypted = encrypt(gettext('hamlet.txt'), 'caesar', 3)
    # txt = open('hamlet_caesar_encrypted.txt', 'w')
    # txt.write(encrypted)
    # decrypted = decrypt(encrypted, 'caesar', 3)
    # decrypted_txt = open('hamlet_caesar_decrypted.txt', 'w')
    # decrypted_txt.write(decrypted)

    # permutation cipher
    encrypted = encrypt(gettext('hamlet.txt'), 'permutation', '9999456')
    txt = open('hamlet_permutation_encrypted.txt', 'w')
    txt.write(encrypted)
    decrypted = decrypt(encrypted, 'permutation', '9999456')
    decrypted_txt = open('hamlet_permutation_decrypted.txt', 'w')
    decrypted_txt.write(decrypted)


    