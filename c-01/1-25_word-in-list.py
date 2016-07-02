sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

# Part 25-1
for word in sent:
    if 'sh' in word:
        print(word)

# Part 25-2
for word in sent:
    if len(word) > 4:
        print(word)
