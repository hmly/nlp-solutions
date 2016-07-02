# Chapter 3, ex. 25b - Using this txt, may take up to 1 min to load.

# Import
import nltk
import re

# Function
def txt_to_pigLatin(text):
    pigL_txt = ''
    w_txt = re.findall(r'[a-zA-Z]+', ' '.join(text))

    for word in w_txt:
        const = re.findall(r'^[bcdfghjklmnpqrstvwxyz]+', word.lower())
        if len(const) == 0:
            pigL_txt = pigL_txt + word + 'ay' + ' '
        else:
            w = word.lower().replace(const[0], '')
            pigL_txt = pigL_txt + w + const[0] + 'ay' + ' '
        
    return  pigL_txt[:50]

# Main
txt = nltk.corpus.gutenberg.words('whitman-leaves.txt')
print txt_to_pigLatin(txt)
