from nltk.corpus import cmudict

words = cmudict.entries()
count = 0

for entry in words:
    if len(entry[1]) > 1:
        count += 1

# Percentage of words with more than one possible pronunciation
print(1.0 * count / len(words))