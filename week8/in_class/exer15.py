"""
Exercise 15 — Filter Even Numbers
Write a function get_evens(lst) that returns a new list containing only the even numbers
from lst.
Call the function and print the resulting list.
"""


def get_evens(lst):
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
    return evens


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = get_evens(numbers)

# Alternative: using list comprehension
# even_numbers = [num for num in numbers if num % 2 == 0]

print(f"The even numbers in the list {numbers} are {even_numbers}.")
