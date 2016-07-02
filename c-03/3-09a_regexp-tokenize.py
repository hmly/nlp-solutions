# Chapter 3 - exercise 9 and 9a

# Import
import nltk
from urllib import urlopen

# Function
def load(f):
    text = urlopen(f).read()
    return text

# Main
pattern = r'''(?x)
        ([A-Z]\.)+
        | \w+(-\w+)*
        | \$?\d+(\.\d+)?%?
        | \.\.\.
        | [][.,;"'?():-_`]
        '''
print nltk.regexp_tokenize(load('corpus.txt'), pattern)
