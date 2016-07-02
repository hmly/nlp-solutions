# Chapter 3 - exercise 21

# Imports
import nltk
import re
from urllib import urlopen

# Function
def unknown(url):
    raw = urlopen(url).read()
    text = nltk.clean_html(raw)
    words = re.findall(r'[A-Za-z]+', text)

    for w in set(words):
        if w.lower() in nltk.corpus.words.words():
            words.remove(w)
    
    return sorted(set(words))

# unknown('http://google.com/')
