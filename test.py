import caesar_cipher as caesar
import permutation_cipher as permutation
from keyprocess import key_process




if __name__ == '__main__':
    key = "4231"
    key = key_process(key, 'permutation', False)
    print(key)

    with open('hamlet.txt', 'r') as file:
        text = file.read()


    # text = "HELLO WORLD"
    # print(text)
    encrypted_text = permutation.encrypt(text, key, True)

    # decrypted_text = permutation.decrypt(encrypted_text, key, True)

    decrypted_text, key = permutation.decrypt_without_key(encrypted_text, True)

    # for line in decrypted_text.split('\n'):
    #     print(line)

    print('Correct key:', key)