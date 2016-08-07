from nltk.corpus import brown

prnt_format = '%14s %8d %8d %7.2f'

print('%14s %8s %8s %20s' % ('Genre', 'Tokens',
                             'Types', 'Lexical Diversity'))
for genre in brown.categories():
    tokens = brown.words(categories=genre)
    print(prnt_format % (genre, len(tokens), len(set(tokens)),
                         1.0 * len(tokens) / len(set(tokens))))
