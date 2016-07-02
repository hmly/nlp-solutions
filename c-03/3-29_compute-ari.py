from nltk.corpus import brown

catgs = ['lore', 'learned', 'humor']
words = [brown.words(categories='lore'), brown.words(categories='learned'),
         brown.words(categories='humor')]
sents = [brown.sents(categories='lore'), brown.sents(categories='learned'),
         brown.sents(categories='humor')]

# Compute ARI
for n in range(len(catgs)):
    u_w = sum([len(w) for w in words[n]])*1.0/len(words[n])
    u_s = sum([len(w) for w in sents[n]])*1.0/len(sents[n])
    print('Section of Brown Corpus:', catgs[n], '\nARI:', 4.71*u_w + 0.5*u_s - 21.43)
