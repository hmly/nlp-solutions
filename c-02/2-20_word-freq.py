from nltk.corpus import brown


# Returns the frequency of the word in the specified genre.
def word_freq(word, genre):
    c = 0
    for w in brown.words(categories=genre):
        if w == word:
            c += 1
    return c


print(word_freq('Fulton', 'news'))
print(word_freq('lol', 'government'))
print(word_freq('the', 'religion'))
print(word_freq('county', 'news'))
print(word_freq('love', 'romance'))
