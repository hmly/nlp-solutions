def vocab_size(text):
    return len(sorted(set(text)))

print(vocab_size('The quick brown fox jumps over the lazy dog'))