from math import log10


class ngram_score(object):
    def __init__(self, ngramfile, sep=' '):
        # load a file containing ngrams and counts, calculate log probabilities
        self.ngrams = {}  # store ngrams and their counts
        with open(ngramfile, 'r') as file:
            for line in file:
                key, count = line.split(sep)  # divide the ngram and its count
                self.ngrams[key] = int(count)  # store the ngram and its count
        self.L = len(key)  # length of ngram
        self.N = sum(self.ngrams.values())  # total number of ngrams
        # calculate the log probability of ngrams
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(
                float(self.ngrams[key]) / self.N)  # calculate the log probability of ngrams
        self.floor = log10(0.01 / self.N)  # calculate the log probability threshold

    def score(self, text):
        # compute the score of a text
        score = 0
        ngrams = self.ngrams.__getitem__  # get the value of ngrams
        for i in range(len(text) - self.L + 1):
            if text[i:i+self.L] in self.ngrams:
                score += ngrams(text[i:i+self.L])  
            else:
                score += self.floor  # if the ngram is not in the ngrams, add the threshold
        return score