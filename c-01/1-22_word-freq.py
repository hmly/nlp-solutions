import nltk
from nltk.book import *

fdist = nltk.FreqDist([w.lower() for w in text5 if len(w) == 4])
print(fdist.most_common())
