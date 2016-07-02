# Chapter 3 - exercise 19

# Variables
raw = open('my_file.txt').readlines()
my_list = []

# Convert to New List
for t in raw:
    t = t.split()
    my_list += [[t[0], int(t[1])]]

print my_list    
