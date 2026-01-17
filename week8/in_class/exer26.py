"""
Exercise 26 — Check If List Has Duplicates
Write a function
has_duplicates(lst)
that returns True if lst contains at least one value appearing more than once, and False
otherwise.
In main:
● Test the function with: a list with duplicates and a list with all unique values.
● Print clear messages for each test.
"""


def has_duplicates(lst):
    seen = {}  # dictionary to track seen items
    for item in lst:
        if item in seen:
            return True
        seen[item] = True
    return False


# Main program
list_with_duplicates = [1, 2, 3, 4, 5, 3]
list_unique = [1, 2, 3, 4, 5]
print("List with duplicates has duplicates:", has_duplicates(list_with_duplicates))
print("List with unique values has duplicates:", has_duplicates(list_unique))
