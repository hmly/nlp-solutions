# Chapter 3 - exercise 18

# Imports
import nltk
from nltk.corpus import gutenberg

# Chose texts from gutenberg.fileids()
# Tokenize
text = gutenberg.raw('chesterton-ball.txt')
tokens = nltk.word_tokenize(text)

# Print 'wh' tokens in order
print sorted(set([w for w in tokens if w.startswith('wh')]))
