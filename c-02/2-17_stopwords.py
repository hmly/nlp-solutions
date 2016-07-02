# Chapter 2 - exercise 17

# Imports
import nltk
from nltk.corpus import stopwords
from nltk.book import*

# Fuction
def freq_50_not_stopwords(text):
    freq = nltk.FreqDist([w for w in text if w.lower() not in stopwords.words('english')])
    print freq.keys()[:50]
    
