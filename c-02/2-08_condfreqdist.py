# Chapter 2 - exercise 8

import nltk

names = nltk.corpus.names
male_names = names.words('male.txt')
female_names = names.words('female.txt')

# Check the first letter of the name
cfd = nltk.ConditionalFreqDist(
    (fileid, name[0])
    for fileid in names.fileids()
    for name in names.words(fileid))

cfd.plot()
