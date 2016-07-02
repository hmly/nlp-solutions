from nltk.book import *

# Part 24-1
print([w for w in set(text6) if w.endswith('ize')])

# Part 24-2
print([w for w in set(text6) if 'z' in w])

# Part 24-3
print([w for w in set(text6) if 'pt' in w])

# Part 24-4
print([w for w in text6 if w.islower() or w.istitle()])
