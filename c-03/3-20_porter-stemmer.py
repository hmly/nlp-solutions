# Chapter 3, exercise 30

# Imports
import nltk

# Main
text = '''Dreaming and loving the world intertwined between past
        and future. Men and women traveling across rivers and
        mountains, lost in unbearable lands.'''
tokens = nltk.word_tokenize(text)

porter = nltk.PorterStemmer()
print 'Porter Stemmer\n', [porter.stem(w) for w in tokens]

lancaster = nltk.LancasterStemmer()
print'Lancaster Stemmer\n', [lancaster.stem(w) for w in tokens]
