import nltk
from nltk.book import*

def prominent(t1, t2):
    fd1 = FreqDist(t1)
    fd2 = FreqDist(t2)
    print sorted([[fd1.freq(w) - fd2.freq(w), w] for w in set(fd1.keys() + fd2.keys())])[-25:]