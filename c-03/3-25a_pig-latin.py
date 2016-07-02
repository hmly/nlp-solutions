import re


def wrd_to_piglatin(word):
    const = re.findall(r'^[bcdfghjklmnpqrstvwxyz]+', word.lower())
    if len(const) == 0:
        w = word + 'ay'
    else:
        w = word.lower().replace(const[0], '', 1)
        w = w + const[0] + 'ay'
    return  w

print(wrd_to_piglatin('by'))
