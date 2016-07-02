import nltk
from urllib import urlopen

url = 'http://www.yahoo.com/'

# Extract contents from web page
html = urlopen(url).read()
raw = nltk.clean_html(html)
tokens = nltk.word_tokenize(raw)
contents = nltk.Text(tokens)

# Display the 'Trending Now' topics (10)
print(contents[contents.index('Trending'):contents.index('in')])
