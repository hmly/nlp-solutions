import nltk
from nltk.corpus import stopwords


def freq_50_not_stopwords(text):
    freq = nltk.FreqDist([w for w in text if w.lower() not in stopwords.words('english')])
    print(freq.keys()[:50])
