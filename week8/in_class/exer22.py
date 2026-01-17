"""
Exercise 22 — Check If List Is Strictly Increasing
Write a function
is_strictly_increasing(lst)
that returns True if each element in lst is strictly greater than the previous one, and
False otherwise.
In main:
● Test the function with at least two different lists and print the results.
"""


def is_strictly_increasing(lst):
    for i in range(1, len(lst)):
        if lst[i] <= lst[i - 1]:
            return False
    return True


# Main program
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 2, 4, 5]
print(is_strictly_increasing(list1))  # Expected: True
print(is_strictly_increasing(list2))  # Expected: False
