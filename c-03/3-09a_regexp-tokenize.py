import nltk
from urllib import urlopen


def load(f):
    text = urlopen(f).read()
    return text

pattern = r'''(?x)
        ([A-Z]\.)+
        | \w+(-\w+)*
        | \$?\d+(\.\d+)?%?
        | \.\.\.
        | [][.,;"'?():-_`]
        '''
print(nltk.regexp_tokenize(load('corpus.txt'), pattern))
