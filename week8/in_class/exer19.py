"""
Exercise 19 — Word Frequency Counter
Write a function word_frequency(text) that:
1. Splits the sentence into words
2. Creates a dictionary where keys are words and values are the number of
occurrences
Return the dictionary.
In main, input a sentence, call the function, and print the dictionary.

"""


def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        word = word.lower()  # Normalize to lowercase
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1  # First occurrence
    return frequency


# Example usage
sentence = input("Enter a sentence: ")
freq_dict = word_frequency(sentence)
print("Word Frequency Dictionary:")
for word, count in freq_dict.items():
    print(f"{word}: {count}")
