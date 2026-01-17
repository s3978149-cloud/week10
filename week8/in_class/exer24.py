"""
Exercise 24 — Filter Dictionary by Minimum Value
Write a function
filter_by_min_value(d, threshold)
that takes a dictionary d mapping strings to numbers and returns a new dictionary
containing only the key–value pairs where the value is greater than or equal to
threshold.
In main:
● Create a dictionary of at least 5 items (e.g., product → price, name → score).
● Ask the user for a threshold.
● Call the function and print the filtered dictionary.
"""


def filter_by_min_value(d, threshold):
    filtered_dict = {}
    for key, value in d.items():
        if value >= threshold:
            filtered_dict[key] = value
    return filtered_dict


# Main program
items = {"apple": 1.2, "banana": 0.5, "cherry": 2.5, "date": 3.0, "elderberry": 1.8}
threshold_value = float(input("Enter the minimum value threshold: "))
filtered_items = filter_by_min_value(items, threshold_value)
print("Filtered dictionary:", filtered_items)
