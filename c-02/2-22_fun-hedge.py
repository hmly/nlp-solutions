from nltk.book import *


# Note: hedge(text)[:N] to avoid printing out the entire new text
def hedge(text):
    text_dp = []
    for w in range(len(text)):
        if w % 3 == 0 and w != 0:
            text_dp.append('like')
        text_dp.append(text[w])    
    return text_dp

print(' '.join(hedge(text1)[:100]))