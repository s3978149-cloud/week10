"""
Exercise 23 — Find All Indices of a Value
Write a function
find_indices(lst, value)
that returns a list of indices where value appears in lst.
In main:
● Define a list with repeated values.
● Ask the user for a value to search for.
● Call the function and print the list of indices.
● If the value does not appear, the returned list should be empty.
"""


def find_indices(lst, value):
    indices = []
    for index in range(len(lst)):
        if lst[index] == value:
            indices.append(index)
    return indices


# Main program
values = [3, 5, 3, 7, 9, 3, 2]
search_value = int(input("Enter a value to search for: "))
result_indices = find_indices(values, search_value)
print("Indices where the value appears:", result_indices)
