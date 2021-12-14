"""
CP1404 Practicals
Count word occurrences and print it
"""

word_occurrences = {}
user_input = input("Enter text: ")

words = user_input.split()
for word in words:
    frequency = word_occurrences.get(word, 0)
    word_occurrences[word] = frequency + 1

words = list(word_occurrences.keys())
words.sort()

max_length = max(len(word) for word in words)
for word in words:
    print(f"{word:{max_length}} : {word_occurrences[word]}")
