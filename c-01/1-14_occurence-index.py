sent3 = ['In', 'the', 'beginning', 'God', 'created', 'the', 'heaven',
         'and', 'the', 'earth', '.']
keyword = 'the'

print(sent3.index(keyword))          # index of 1
print(sent3[2:].index(keyword) + 2)  # index of 3 + 2 displacement due to slicing
print(sent3[4:].index(keyword) + 7)  # index of 1 + 7 displacement due to slicing
