import cipher.caesar_cipher as caesar
import cipher.permutation_cipher as permutation
import cipher.substitution_cipher as substitution
from flask import Flask, render_template, request, jsonify
import modules.cipher_key as cipher_key


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


@app.route('/features')
def features():
    title = 'Features'
    name = 'Features'
    return render_template('features.html', title=title, name=name)

def gettext(path="hamlet.txt"):  # get text from file
    text = open(path, "r").read()
    return text


def encrypt(text, method, key=0, casesensitive=True):  # encrypt text
    if method == 'caesar':
        return caesar.encrypt(text, key, casesensitive)
    if method == 'permutation':
        return permutation.encrypt(text, key, casesensitive)
    if method == 'substitution':
        return substitution.encrypt(text, key, casesensitive)


def decrypt(text, method, key, casesensitive):  # decrypt text
    if method == 'caesar':
        return caesar.decrypt(text, key, casesensitive)
    if method == 'permutation':
        return permutation.decrypt(text, key, casesensitive)
    if method == 'substitution':
        return substitution.decrypt(text, key, casesensitive)
    

def encrypt_without_key(text, method, casesensitive):  # encrypt text without key
    key = cipher_key.key(method=method).randomkey()
    if method == 'caesar':
        return caesar.encrypt(text, key, casesensitive), key
    if method == 'permutation':
        return permutation.encrypt(text, key, casesensitive), key
    if method == 'substitution':
        return substitution.encrypt(text, key, casesensitive), key
    
    
def decrypt_without_key(text, method, casesensitive):  # decrypt text without key
    if method == 'caesar':
        return caesar.decrypt_without_key(text, casesensitive)
    if method == 'permutation':
        return permutation.decrypt_without_key(text, casesensitive)
    if method == 'substitution':
        return substitution.decrypt_without_key(text, casesensitive)


@app.route('/encrypt', methods=['GET','POST'])
def encryptpage():
    data = request.json # get data from request
    plaintext = data['plaintext']
    method = data['ciphermethod']
    casesensitive = data['casesensitive']
    keyprocess = data['keyprocess']

    cipherkey = cipher_key.key(data['key'], method)

    if not keyprocess:
        if not cipherkey.check(method):
            return jsonify(status=False, message='Invalid key')
        
    if data['withoutKey']:
        ciphertext, key = encrypt_without_key(plaintext, method, casesensitive)
        
    key = cipherkey.process(keyprocess)
    print(key)

    ciphertext = encrypt(plaintext, method, key, casesensitive)
    return jsonify(ciphertext=ciphertext, key=key)


@app.route('/decrypt', methods=['GET','POST'])
def decryptpage():
    data = request.json
    ciphertext = data['ciphertext']
    method = data['ciphermethod']
    casesensitive = data['casesensitive']
    keyprocess = data['keyprocess']

    cipherkey = cipher_key.key(data['key'], method)

    if data['withoutKey']:
        plaintext, key = decrypt_without_key(ciphertext, method, casesensitive)
        return jsonify(plaintext=plaintext, key=key)
    

    if not keyprocess:
        if not cipherkey.check(method):
            return jsonify(status=False, message='Invalid key')
        

    key = cipherkey.process(keyprocess)
    print(key)

    plaintext = decrypt(ciphertext, method, key, casesensitive)
    return jsonify(plaintext=plaintext, key=key)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    


    