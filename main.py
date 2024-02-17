import caesar_cipher as caesar
import permutation_cipher as permutation
from keyprocess import key_process
from flask import Flask, render_template, request, jsonify


def gettext(path="hamlet.txt"):  # get text from file
    text = open(path, "r").read()
    return text


def encrypt(text, method, key=0, casesensitive=True):  # encrypt text
    if method == 'caesar':
        return caesar.encrypt(text, key, casesensitive)
    if method == 'permutation':
        return permutation.encrypt(text, key, casesensitive)


def decrypt(text, method, key=0):  # decrypt text
    if method == 'caesar':
        return caesar.decrypt(text, key)
    if method == 'permutation':
        return permutation.decrypt(text, key)


app = Flask(__name__, static_folder="static")

@app.route('/')
def index():
    title = 'Home'
    name = 'Home'
    return render_template('index.html', title=title, name=name)

@app.route('/termsofuse')
def termsofuse():
    title = 'Terms of Use'
    name = 'Terms of Use'
    return render_template('terms_of_use.html', title=title, name=name)

@app.route('/privacypolicy')
def privacypolicy():
    title = 'Privacy Policy'
    name = 'Privacy Policy'
    return render_template('privacy_policy.html', title=title, name=name)


@app.route('/contact')
def contact():
    title = 'Contact'
    name = 'Contact'
    return render_template('contact.html', title=title, name=name)


@app.route('/encrypt', methods=['GET','POST'])
def encryptpage():
    data = request.json  # 获取JSON数据
    plaintext = data['plaintext']
    method = data['ciphermethod']
    casesensitive = data['casesensitive']
    keyprocess = data['keyprocess']
    key = key_process(data['key'], method, keyprocess)
    ciphertext = encrypt(plaintext, method, key, casesensitive)
    print(key)
    return jsonify(ciphertext=ciphertext)


@app.route('/decrypt', methods=['GET','POST'])
def decryptpage():
    data = request.json
    ciphertext = data['ciphertext']
    method = data['ciphermethod']
    keyprocess = data['keyprocess']
    key = key_process(data['key'], method, keyprocess)
    plaintext = decrypt(ciphertext, method, key)
    return jsonify(plaintext=plaintext)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    


    