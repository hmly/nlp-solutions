# Chapter 3, ex. 25a

# Import
import re

# Function
def wrd_to_pigLatin(word):
    const = re.findall(r'^[bcdfghjklmnpqrstvwxyz]+', word.lower())
    if len(const) == 0:
        w = word + 'ay'
    else:
        w = word.lower().replace(const[0], '', 1)
        w = w + const[0] + 'ay'
    return  w

# Main
print wrd_to_pigLatin('by')
