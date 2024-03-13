from pycipher import SimpleSubstitution as SimpleSub
import random
import re
from ngram_score import ngram_score
from check_words import check_english
from substitution_cipher import decrypt, encrypt
fitness = ngram_score('quadgrams.txt') # load our quadgram statistics

ptext='AGAIN PIERRE WAS OVERTAKEN BY THE DEPRESSION HE SODREADED FOR THREE DAYS AFTER THE DELIVERY OF HIS SPEECH AT THE LODGE HELAYONA SO FA AT HOME RECEIVING NO ONE AND GOING NO WHERE'
entext = encrypt(ptext, 'PHQGIUMEAJLNOFDXVKRCYSTZWB')
ctext = re.sub('[^A-Z]','',entext.upper())

maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
maxscore = -99e9
parentscore,parentkey = maxscore,maxkey[:]
# print "Substitution Cipher solver, you may have to wait several iterations"
# print "for the correct result. Press ctrl+c to exit program."
# keep going until we are killed by the user
i = 0
detext = SimpleSub(parentkey).decipher(entext)
while not check_english(detext):
    i = i+1
    random.shuffle(parentkey)
    deciphered = SimpleSub(parentkey).decipher(ctext)
    parentscore = fitness.score(deciphered)
    count = 0
    while count < 1000:
        a = random.randint(0,25)
        b = random.randint(0,25)
        child = parentkey[:]
        # swap two characters in the child
        child[a],child[b] = child[b],child[a]
        deciphered = SimpleSub(child).decipher(ctext)
        score = fitness.score(deciphered)
        # if the child was better, replace the parent with it
        if score > parentscore:
            parentscore = score
            parentkey = child[:]
            count = 0
        count = count+1
    # keep track of best score seen so far
    if parentscore>maxscore:
        maxscore,maxkey = parentscore,parentkey[:]
        print ('\nbest score so far:',maxscore,'on iteration',i)
        ss = SimpleSub(maxkey)
        print ('    best key: '+''.join(maxkey))
        print ('    plaintext: '+ss.decipher(ctext))
        detext = decrypt(entext, maxkey)
        print ('    decrypted text: '+detext)

