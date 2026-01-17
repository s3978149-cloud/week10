"""
Exercise 11 — Sum of List
Write a function sum_list(lst) that returns the sum of all numbers in the list lst.
In the main program, define a list of at least 5 integers, call the function, and print the
returned sum.
"""


def sum_list(lst):
    total = 0
    for num in lst:
        total += num
    return total


numbers = [10, 20, 30, 40, 50]
result = sum_list(numbers)

# Alternative: using built-in sum function
# result = sum(numbers)

print(f"The sum of the list {numbers} is {result}.")
