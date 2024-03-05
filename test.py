import caesar_cipher as caesar
import permutation_cipher as permutation
import substitution_cipher as substitution
from keyprocess import key_process
import random_key




if __name__ == '__main__':
    key = "EJOTYCHMRWFLNBXDPUVZGKQIAS"
    # key = key_process(key, 'permutation', False)
    print(key)

    # with open('hamlet.txt', 'r') as file:
    #     text = file.read()

    print(random_key.substitution())

    text = "HELLO WOrLD"
    # print(text)
    encrypted_text = substitution.encrypt(text, key, False)

    # print(encrypted_text)

    decrypted_text = substitution.decrypt(encrypted_text, key, True)

    # print(decrypted_text)

    # decrypted_text, key = permutation.decrypt_without_key(encrypted_text, True)

    # # for line in decrypted_text.split('\n'):
    # #     print(line)

    # print('Correct key:', key)