import caesar_cipher as caesar
import permutation_cipher as permutation
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify


def gettext(path="hamlet.txt"):  # get text from file
    text = open(path, "r").read()
    return text

def key_process(number_strings):
    number_strings = ''.join([str(ord(char)) if char.isalpha() else char for char in number_strings])
    number_strings = str(int(number_strings)*int(number_strings)*len(number_strings))
    print(number_strings)
    appeared = set()
    unique = []
    for number in number_strings:
        if number not in appeared:
            unique.append(number)
            appeared.add(number)
    number_strings = unique
    numbers = [int(s) for s in number_strings]
    sorted_numbers = sorted(numbers)
    processed = []
    for number in number_strings:
        index = sorted_numbers.index(int(number))
        processed.append(index)
    print(processed)
    # to int
    processed = ''.join([str(i) for i in processed])
    return processed

def encrypt(text, method, key=0, casesensitive=True):  # encrypt text
    if method == 'caesar':
        return caesar.encrypt(text, int(key), casesensitive)
    if method == 'permutation':
        return permutation.encrypt(text, key, casesensitive)


def decrypt(text, method, key=0):  # decrypt text
    if method == 'caesar':
        return caesar.decrypt(text, int(key))
    if method == 'permutation':
        return permutation.decrypt(text, int(key))


app = Flask(__name__)

@app.route('/')
def index():
    title = 'Home'
    name = 'Home'
    return render_template('webUI.html', title=title, name=name)


@app.route('/encrypt', methods=['GET','POST'])
def encryptpage():
    data = request.json  # 获取JSON数据
    plaintext = data['plaintext']
    key = data['key']
    key = key_process(key)
    method = data['ciphermethod']
    casesensitive = data['casesensitive']
    ciphertext = encrypt(plaintext, method, key, casesensitive)
    # 这里添加你的加密逻辑，下面是一个示例
    print(key, method, casesensitive)
    return jsonify(ciphertext=ciphertext)


if __name__ == '__main__':

    # caesar cipher
    # encrypted = encrypt(gettext('hamlet.txt'), 'caesar', 3)
    # txt = open('hamlet_caesar_encrypted.txt', 'w')
    # txt.write(encrypted)
    # decrypted = decrypt(encrypted, 'caesar', 3)
    # decrypted_txt = open('hamlet_caesar_decrypted.txt', 'w')
    # decrypted_txt.write(decrypted)

    # permutation cipher
    # encrypted = encrypt(gettext('hamlet.txt'), 'permutation', '9999456')
    # txt = open('hamlet_permutation_encrypted.txt', 'w')
    # txt.write(encrypted)
    # decrypted = decrypt(encrypted, 'permutation', '9999456')
    # decrypted_txt = open('hamlet_permutation_decrypted.txt', 'w')
    # decrypted_txt.write(decrypted)

    app.run(host='127.0.0.1', port=8080, debug=True)


    