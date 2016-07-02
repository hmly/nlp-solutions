from nltk.corpus import wordnet as wn

"""Display holonym-meronym relations
holonyms: things an item is contained in
meronyms: an item components
member: a tree is a member of a forest
part: trunk is a part of a tree
substance: a tree is made of heartwood
"""
nouns = ['fish', 'animal', 'tree', 'water', 'wood']
for noun in nouns:
    syn = wn.synsets(noun)[0]
    print(syn)

    print(syn.member_meronyms())
    print(syn.part_meronyms())
    print(syn.substance_meronyms())

    print(syn.member_holonyms())
    print(syn.part_holonyms())
    print(syn.substance_holonyms())
