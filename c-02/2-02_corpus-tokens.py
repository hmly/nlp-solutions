from nltk.corpus import gutenberg

austen = gutenberg.words('austen-persuasion.txt')
print('num of tokens:', len(austen))
print('num of words:', len(set(austen)))
