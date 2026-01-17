"""
Exercise 18 — Invert Dictionary (Swap Keys & Values)
Write a function invert_dict(d) that returns a new dictionary where each value becomes
its key and each key becomes its value.
Assume all values are unique.
Call the function and print the result.
"""


def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        inverted[value] = key
    return inverted


# Example usage
original_dict = {"name": "Alice", "age": 30, "city": "New York"}
inverted_dict = invert_dict(original_dict)

# Alternative: using dictionary comprehension
# inverted_dict = {value: key for key, value in original_dict.items()}

print("Original dictionary:", original_dict)
print("Inverted dictionary:", inverted_dict)
