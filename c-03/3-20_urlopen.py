# Chapter 3 - exercise 20

# Imports
import nltk
from urllib import urlopen

# Variables
url = 'http://www.yahoo.com/'

# Extract Contents From Web Page
html = urlopen(url).read()
raw = nltk.clean_html(html)

tokens = nltk.word_tokenize(raw)
contents = nltk.Text(tokens)

# Print the 'Trending Now' topics (10); include numbers (1-10)
print contents[contents.index('Trending'):contents.index('in')]

