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

    
def decrypt_without_key(text, method):  # decrypt text without key
    if method == 'caesar':
        return caesar.decrypt_without_key(text)
    if method == 'permutation':
        return permutation.decrypt_without_key(text)
    if method == 'substitution':
        return substitution.decrypt_without_key(text)


@app.route('/encrypt', methods=['GET','POST'])
def encryptpage():
    data = request.json # get data from request
    plaintext = data['plaintext']
    method = data['ciphermethod']
    casesensitive = data['casesensitive']
    keyprocess = data['keyprocess']

    cipherkey = cipher_key.key(data['key'], method)
        
    if data['withoutKey']:
        key = cipherkey.randomkey()
    else:
        key = data['key']
        
    processedkey = cipherkey.process(keyprocess)

    print(processedkey)

    if not cipherkey.check(method):
        return jsonify(status=False)
    

    ciphertext = encrypt(plaintext, method, processedkey, casesensitive)

    return jsonify(ciphertext=ciphertext, key=key, status=True)


@app.route('/decrypt', methods=['GET','POST'])
def decryptpage():
    data = request.json
    ciphertext = data['ciphertext']
    method = data['ciphermethod']
    casesensitive = data['casesensitive']
    keyprocess = data['keyprocess']

    cipherkey = cipher_key.key(data['key'], method)

    if data['withoutKey']:
        key = decrypt_without_key(ciphertext, method)
        cipherkey.key = key
    else:
        key = data['key']

    processedkey = cipherkey.process(keyprocess)

    if not cipherkey.check(method):
        return jsonify(status=False)
    

    plaintext = decrypt(ciphertext, method, processedkey, casesensitive)
    return jsonify(plaintext=plaintext, key=key, status=True)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    


    