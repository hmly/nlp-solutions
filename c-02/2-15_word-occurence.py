# Chapter 2 - exercise 15

# Imports
import nltk
from nltk.corpus import brown

# Declaring the variables
words_3 = []
fd = nltk.FreqDist(brown.words())

# Loop - each token must occur at least 3 times to be added to words_3
for w in fd.keys():
    if fd[w] >= 3:
        words_3.append(w)

