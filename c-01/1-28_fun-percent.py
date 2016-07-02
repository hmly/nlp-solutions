def percent(word, text):
    return 100.0 * text.lower().count(word.lower()) / len(text)

print(percent('the', 'The quick brown fox jumps over the lazy dog'))