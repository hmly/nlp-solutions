import nltk
import re

# Letter Values
letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
    'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
    'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}


def gematria(txt, t_list):
    w_cnt = sum = 0
    str_txt = ' '.join(txt)  # Convert txt to str
    text = re.findall(r'[a-zA-Z]+', str_txt)  # Exclude punctuations
    
    for w in text: 
        for c in w.lower():
            sum += letter_vals[c]
        if sum == 666:
            w_cnt += 1
        sum = 0
    return w_cnt

texts_list = nltk.corpus.state_union.fileids()
c = -1
print('Document'.ljust(20), 'Words Count\n')
for t in texts_list:
    print(texts_list[c].ljust(20),  # Doc name
          gematria(nltk.corpus.state_union.words(t), texts_list))  # Num of words with 666 val
    c += 1
