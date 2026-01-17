"""
Exercise 30 — Check If Dictionary Values Are Sorted
Write a function
are_values_sorted(d)
that takes a dictionary d whose values are numbers and returns True if the values, in the
order of their keys sorted alphabetically, form a non-decreasing sequence. Otherwise,
return False.
Steps inside the function:
1. Get a sorted list of keys.
2. Build a list of corresponding values in that key order.
3. Check if this value list is non-decreasing.
In main:
● Create at least two different dictionaries to test (one that satisfies the property and
one that does not).
● Call the function for each and print the result
"""


def are_values_sorted(d):
    sorted_keys = sorted(d.keys())  # Get sorted list of keys
    values_in_order = [d[key] for key in sorted_keys]

    for i in range(1, len(values_in_order)):
        if values_in_order[i] < values_in_order[i - 1]:
            return False
    return True


# Main program
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"a": 3, "b": 2, "c": 1}

print("Are values sorted in dict1?", are_values_sorted(dict1))
print("Are values sorted in dict2?", are_values_sorted(dict2))
