"""
Exercise 16 — Print Dictionary Keys and Values
Write a function display_dict(d) that prints each key and its value on a separate line in
the form:
key: value
In main, create a dictionary with at least 4 key–value pairs and call the function.

"""


def display_dict(d):
    for key, value in d.items():
        print(f"{key}: {value}")
    # Alternative: using keys() and indexing
    # for key in sample_dict.keys():
    #     print(f"{key}: {sample_dict[key]}")


# Creating a dictionary with at least 4 key-value pairs
sample_dict = {"name": "Alice", "age": 30, "city": "New York", "occupation": "Engineer"}
# Calling the function to display the dictionary
display_dict(sample_dict)
