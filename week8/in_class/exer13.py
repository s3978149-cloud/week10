"""
Exercise 13 — Reverse List (No reverse())
Write a function reverse_list(lst) that returns a new list containing the elements of
lst in reverse order.
Call the function and print the reversed list.
"""


def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst = [item] + reversed_lst
    return reversed_lst


numbers = [1, 2, 3, 4, 5]
reversed_numbers = reverse_list(numbers)


# Alternative: using slicing
# reversed_numbers = numbers[::-1]

print(f"The reversed list of {numbers} is {reversed_numbers}.")
