# Chapter 4, ex. 16a

# Letter Values
letter_vals = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':80, 'g':3, 'h':8,
    'i':10, 'j':10, 'k':20, 'l':30, 'm':40, 'n':50, 'o':70, 'p':80, 'q':100,
    'r':200, 's':300, 't':400, 'u':6, 'v':6, 'w':800, 'x':60, 'y':10, 'z':7}

# Function
def gematria(word):
    return sum([letter_vals[char.lower()] for char in word])

# Main
word = 'python'
print 'Gematria Value: ', gematria(word)
