import caesar_cipher as caesar
import permutation_cipher as permutation
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify


def gettext(path="hamlet.txt"):  # get text from file
    text = open(path, "r").read()
    return text


def encrypt(text, method, key=0, casesensitive=True):  # encrypt text
    if method == 'caesar':
        return caesar.encrypt(text, int(key), casesensitive)
    if method == 'permutation':
        return permutation.encrypt(text, key, casesensitive)


def decrypt(text, method, key=0):  # decrypt text
    if method == 'caesar':
        return caesar.decrypt(text, int(key))
    if method == 'permutation':
        return permutation.decrypt(text, key)


def key_process(number_strings, keyprocess=False):
    if not keyprocess:
        number_strings = ''.join([str(int(char)-1) for char in number_strings])
        return number_strings
    number_strings = ''.join([str(ord(char)) if char.isalpha() else char for char in number_strings])
    number_strings = str(int(number_strings)*int(number_strings)*len(number_strings))
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
    # to int
    processed = ''.join([str(i) for i in processed])
    return processed


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
    method = data['ciphermethod']
    casesensitive = data['casesensitive']
    keyprocess = data['keyprocess']
    key = key_process(data['key'], keyprocess)
    ciphertext = encrypt(plaintext, method, key, casesensitive)
    print(key)
    return jsonify(ciphertext=ciphertext)


@app.route('/decrypt', methods=['GET','POST'])
def decryptpage():
    data = request.json
    ciphertext = data['ciphertext']
    method = data['ciphermethod']
    keyprocess = data['keyprocess']
    key = key_process(data['key'], keyprocess)
    plaintext = decrypt(ciphertext, method, key)
    return jsonify(plaintext=plaintext)


if __name__ == '__main__':

    app.run(host='127.0.0.1', port=8080, debug=True)


    