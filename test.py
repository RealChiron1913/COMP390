import caesar_cipher as caesar
import permutation_cipher as permutation
import substitution_cipher as substitution
from keyprocess import key_process
import random_key
import ngram_score as ns




if __name__ == '__main__':
    key =           "QWERTYUIOPASDFGHJKLZXCVBNM"
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # key = key_process(key, 'permutation', False)

    with open('hamlet.txt', 'r') as file:
        text = file.read()

    # text = "Smith's boyfriend, Andrew Moore, posted a video to her TikTok account Tuesday sharing the news with her followers. The video has gotten over 800,000 likes since being posted on the social media platform.The video has also been commented on over 60,000 times, with many showing support and passing along condolences to Smith's family and loved ones.According to the BBC, Smith had complained of back pain about 10 months before her diagnosis, but it was not until she lost feeling in her left leg that she knew something was wrong."
    encrypted = substitution.encrypt(text, key, True)


    decrypted, key1 = substitution.decrypt_without_key(encrypted, True)

    print(key)
    print(key1)



    # print(decrypted)





