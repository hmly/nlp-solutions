from nltk.book import *

# Find sum of the length of all words in text1
print(sum(len(w) for w in text1))

# Find the average word length of any text (in this case, text1)
print(sum(len(w) for w in text1) * 1.0 / len(text1))