from caesar_cipher import *


def gettext(path="hamlet.txt"):  # get text from file
    text = open(path, "r").read()
    return text


if __name__ == '__main__':
    key = 3
    caesar_encrypted = caesar_encrypt(gettext('hamlet.txt'), key)
    txt = open('hamlet_caesar_encrypted.txt', 'w')
    txt.write(caesar_encrypted)

    caesar_decrypted_without_key = caesar_decrypt_without_key(gettext('hamlet_caesar_encrypted.txt'))
    txt = open('hamlet_caesar_decrypted_without_key.txt', 'w')
    txt.write(caesar_decrypted_without_key)

    caesar_decrypted = caesar_decrypt(gettext('hamlet_caesar_encrypted.txt'), key)
    txt = open('hamlet_caesar_decrypted.txt', 'w')
    txt.write(caesar_decrypted)
