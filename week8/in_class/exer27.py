"""
Exercise 27 — Find Key with Maximum Value in Dictionary
Write a function
key_of_max_value(d)
that returns the key associated with the largest value in the dictionary d.
Assume the dictionary is non-empty and values are numbers.
In main:
● Create a dictionary of names and scores.
● Call the function and print the name with the highest score.
"""


def key_of_max_value(d):
    max_key = None
    max_value = float("-inf")  # Initialize to negative infinity
    for key, value in d.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key


# Main program
scores = {"Alice": 85, "Bob": 92, "Charlie": 88, "David": 95}
top_scorer = key_of_max_value(scores)
print("The name with the highest score is:", top_scorer)
