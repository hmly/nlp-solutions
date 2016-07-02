# Chapter 2 - exercise 9

# Imports
import nltk
from nltk.book import*

# Compare two texts
print text1, '\n', 'Vocabulary:', len(set(text1)), '\n', 'Vocabulary Richness:', 1.0*len(text1)/len(set(text1))
print text5, '\n', 'Vocabulary:', len(set(text5)), '\n', 'Vocabulary Richness:', 1.0*len(text5)/len(set(text5))

# Pairs of Words with different meaning
# chat and join, game and 
print text1.concordance('chat')
print text5.concordance('chat')

# print text1.concordance('join')
# print text5.concordance('join')

# text1.concordance('game')
# text5.concordance('game')

# text1.concordance('text')
# text5.concordance('text')

#* Remove the # from the four print statements above to
#* understand why the words differ from each text
