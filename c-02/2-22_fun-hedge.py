# Chapter 2 - exercise 22

# Import
import nltk
from nltk.book import*

# Function
def hedge(text):
    text_dp = []
    for w in range(len(text)):
        if w  % 3 == 0 and w != 0:
            text_dp.append('like')
        text_dp.append(text[w])    
    return text_dp

# Note: var = hedge(text) to avoid printing out the entire new text
