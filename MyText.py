def count_words(text):
    words = text.split()
    return len(words)

def words_by_length(text):
    words = text.split()
    return sorted(words, key=len, reverse=True)

def words_alphabetical(text):
    words = text.split()
    return sorted(words, key=str.lower)