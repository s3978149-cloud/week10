"""
Exercise 12 — Maximum Value (No max())
Write a function find_max(lst) that returns the largest element in the list without using
max().
Call the function from main and print the result.

"""


def find_max(lst):
    if not lst:
        return None  # Handle empty list case
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value


numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
maximum = find_max(numbers)

# Alternative: using built-in max function
# maximum = max(numbers)

print(f"The maximum value in the list {numbers} is {maximum}.")