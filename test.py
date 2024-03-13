import caesar_cipher as caesar
import permutation_cipher as permutation
import substitution_cipher as substitution
from keyprocess import key_process
import random_key
import ngram_score as ns




if __name__ == '__main__':
    key =           "EJOTYCHMRWFLNBXDPUVZGKQIAS"
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # key = key_process(key, 'permutation', False)
    print(key)

    with open('hamlet.txt', 'r') as file:
        text = file.read().lower()

    # substitution.frequency_analysis(text)

    # encrypted = substitution.encrypt(text, key, True)

    # substitution.get_key(encrypted)

    fitness = ns.ngram_score('quadgrams.txt')

    print(fitness.score('SOWFBRKAWFCZFSBSCSBQITBKOWLBFXTBKOWLSOXSOXFZWWIBICFWUQLRXINOCIJLWJFQUNWXLFBSZXFBTXAANTQIFBFSFQUFCZFSBSCSBIMWHWLNKAXBISWGSTOXLXTSWLUQLXJBUUWLWISTBKOWLSWGSTOXLXTSWLBSJBUUWLFULQRTXWFXLTBKOWLBISOXSSOWTBKOWLXAKOXZWSBFIQSFBRKANSOWXAKOXZWSFOBUSWJBSBFTQRKAWSWANECRZAWJ'))


    print(fitness.score('GDHMBRIZHMJLMGBGJGBSYOBIDHXBMCOBIDHXGDCGDCMLHHYBYJMHTSXRCYEDJYUXHUMSTEHCXMBGLCMBOCZZEOSYMBMGMSTMJLMGBGJGBYNHQHXEIZCBYGHFGODCXCOGHXTSXCUBTTHXHYGOBIDHXGHFGODCXCOGHXBGUBTTHXMTXSROCHMCXOBIDHXBYGDCGGDHOBIDHXCZIDCLHGBMYSGMBRIZEGDHCZIDCLHGMDBTGHUBGBMOSRIZHGHZEWJRLZHU'))


