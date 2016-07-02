from nltk.corpus import brown, webtext

# Brown corpus
print('Categories:', list(brown.categories()))
print('Brown sample text:\n\t', ' '.join(brown.words(categories='adventure')[:50]))

# Webtext corpus
print()
print('Categories:', webtext.fileids())
print('Webtext sample text:\n\t', ' '.join(webtext.words('firefox.txt')[:50]))
