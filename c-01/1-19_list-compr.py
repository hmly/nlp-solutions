from nltk.book import *

print(len(sorted(set([w.lower() for w in text1]))))
print(len(sorted([w.lower() for w in set(text1)])))

print(len(sorted(set([w.lower() for w in text2]))))
print(len(sorted([w.lower() for w in set(text2)])))

"""The difference between the first two statements is what occurs in
the list comprehension of sorted. The first statement get all the
word in text1, convert it to lowercase, and find all the distinct
words in the list of words. In the second statement,  words are
extracted from a set of distinct words from text1 and converted
to lowercase. The statement that will give the greater number of
words is the latter. This case applies to other texts as well.
"""
