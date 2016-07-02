from nltk.book import *

# Compare two texts
print(text1, '\n', 'Vocabulary:', len(set(text1)), '\n', 'Vocabulary Richness:',
      1.0 * len(text1) / len(set(text1)))
print(text5, '\n', 'Vocabulary:', len(set(text5)), '\n', 'Vocabulary Richness:',
      1.0 * len(text5) / len(set(text5)), '\n')

# Pairs of words with different meaning
print('\n< chat >')
print(text1.concordance('chat', lines=5))
print(text5.concordance('chat', lines=5))

print('\n< join >')
print(text1.concordance('join', lines=5))
print(text5.concordance('join', lines=5))

print('\n< game >')
print(text1.concordance('game', lines=5))
print(text5.concordance('game', lines=5))

print('\n< text >')
print(text1.concordance('text', lines=5))
print(text5.concordance('text', lines=5))
