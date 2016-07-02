import nltk
from nltk.corpus import gutenberg

text = gutenberg.raw('chesterton-ball.txt')
tokens = nltk.word_tokenize(text)

print(sorted(set([w for w in tokens if w.startswith('wh')])))
