# Assignment 7 - 6

# Imports
import random
import unicodedata

# Variables
text = open('my_text.txt').read()

# Functions
def encryptToFile(text, key, fileid):
    random.seed(key)
    list = [chr((ord(w) + random.randint(-127, 127)) % 128) for w in text]
    crypt_text = open(fileid, 'w')
    for w in list:
        crypt_text.write(w)
    crypt_text.close()

def decryptToFile(text, key, fileid):
    random.seed(key)
    txt = open(fileid).read()
    list = [chr((ord(w) - random.randint(-127, 127)) % 128) for w in txt]
    print ''.join(list)


#* Testing
# encryptToFile(text, 9, 'crypt_text.txt')
# decryptToFile(text, 9, 'crypt_text.txt')
