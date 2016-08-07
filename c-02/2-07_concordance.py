from nltk.book import *

# Show different usage of the word "however"
texts = [text1, text2, text3, text4]
for text in texts:
    print(text)
    text.concordance('however')