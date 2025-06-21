"""
Word Occurrences
Estimate: 10 minutes
Actual:      minutes
"""

text_string = input("Text: ")
words = text_string.split()
word_to_count = {}
maximum_word_length = max(len(word) for word in words)

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word in sorted(word_to_count):
    print(f"{word:{maximum_word_length}} : {word_to_count[word]}")
