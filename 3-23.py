import MyText
text = "Jedno jabłko dziennie trzyma lekarza z daleka"

print(f"Text: {text}")

word_count = MyText.count_words(text)
print(f"Number of words: {word_count}")

longest_words = MyText.words_by_length(text)
print(f"Words from the longest: {','.join(longest_words)}")

ordered_words = MyText.words_alphabetical(text)
print(f"Words ordered alphabetically: {','.join(ordered_words)}")