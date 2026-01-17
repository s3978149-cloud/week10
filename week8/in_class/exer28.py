"""
Exercise 28 — Filter Words by Length
Write a function
filter_by_length(words, min_length)
that takes a list of strings words and an integer min_length, and returns a new list
containing only the words whose length is greater than or equal to min_length.
In main:
● Create a list of at least 8 words.
● Ask the user for a minimum length.
● Call the function and print the filtered list.
"""


def filter_by_length(words, min_length):
    filtered_words = []
    for word in words:
        if len(word) >= min_length:
            filtered_words.append(word)
    return filtered_words


# Main program
words_list = [
    "apple",
    "banana",
    "cherry",
    "date",
    "elderberry",
    "fig",
    "grape",
    "honeydew",
]
min_len = int(input("Enter the minimum length of words to filter: "))


filtered_list = filter_by_length(words_list, min_len)
# Alternative using list comprehension# def filter_by_length(words, min_length):
#     retufiltered_list = [word for word in words if len(word) >= min_length]

print("Filtered list:", filtered_list)
