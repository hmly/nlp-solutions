sent = 'The quick brown fox jumps over the lazy dog'.split()

print([w for w in sent if w.isupper()])
print([w for w in sent if not w.islower()])

"""The former checks if all the characters in the word is lower, while
the latter checks if not all the characters are lowercase or in other
words, if there is at least one uppercase.
"""