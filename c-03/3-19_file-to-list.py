raw = open('my_file.txt').readlines()
my_list = []

for t in raw:
    t = t.split()
    my_list += [[t[0], int(t[1])]]

print(my_list)
