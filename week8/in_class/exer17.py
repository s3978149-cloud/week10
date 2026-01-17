"""
Exercise 17 — Merge Two Dictionaries
Write a function merge_dicts(a, b) that returns a new dictionary containing all
key–value pairs from a and b.
If duplicate keys exist, values from dictionary b override.
Call the function and print the merged dictionary
"""


def merge_dicts(a, b):
    merged = {}
    for key, value in a.items():
        merged[key] = value
    # Alternative, use copy:
    # merged = a.copy()

    # Alternative, use dict from dictionary:
    # merged = dict(a)

    # Alternative, use dictionary comprehension:
    # merged = {key: value for key, value in a.items()}

    # Add elements from b one by one, overriding duplicates
    for key, value in b.items():
        merged[key] = value

    # Alternative, use update method:
    # merged.update(b)
    return merged


# Example usage
dict_a = {"name": "Alice", "age": 30}
dict_b = {"age": 35, "city": "New York"}
merged_dict = merge_dicts(dict_a, dict_b)
print("Merged dictionary:", merged_dict)
