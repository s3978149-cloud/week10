"""
Exercise 29 — Group Values by Parity in a Dictionary
Write a function
group_by_parity(lst)
that takes a list of integers and returns a dictionary with exactly two keys:
● "even" → list of all even numbers
● "odd" → list of all odd numbers
In main:
● Define a list of at least 10 integers.
● Call the function.
● Print the resulting dictionary in a readable format.
"""


def group_by_parity(lst):
    parity_dict = {"even": [], "odd": []}
    for num in lst:
        if num % 2 == 0:
            parity_dict["even"].append(num)
        else:
            parity_dict["odd"].append(num)
    return parity_dict


# Main program
numbers_list = [12, 7, 5, 64, 14, 23, 8, 19, 31, 42]
result = group_by_parity(numbers_list)
print("Grouped by parity:", result)
