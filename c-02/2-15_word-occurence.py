import nltk
from nltk.corpus import brown

words3 = []
fd = nltk.FreqDist(brown.words())

# Loop - each token must occur at least 3 times to be added to words3
for w in fd.keys():
    if fd[w] >= 3:
        words3.append(w)

print(words3[:100])