import nltk
from nltk.corpus import brown, stopwords


def freq_50_not_stopwords(text):
    freq = nltk.FreqDist([w for w in text if w.lower() not in stopwords.words('english')])
    print([w for (w, c) in freq.most_common(50)])

freq_50_not_stopwords(brown.words(categories='news'))
