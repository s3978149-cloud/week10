"""
Exercise 21 — Filter Positive and Negative Numbers
Write a function
split_positive_negative(lst)
that takes a list of integers lst and returns two lists:
● one containing only the positive numbers
● one containing only the negative numbers
In the main program:
● Define a list of at least 8 integers (including positive, negative, and zero).
● Call the function.
● Print both resulting lists.

"""


def split_positive_negative(lst):
    positive_numbers = []
    negative_numbers = []
    for num in lst:
        if num > 0:
            positive_numbers.append(num)
        elif num < 0:
            negative_numbers.append(num)
    return positive_numbers, negative_numbers


# Main program
numbers = [10, -5, 0, 3, -1, 7, -8, 2]
positives, negatives = split_positive_negative(numbers)
print("Positive numbers:", positives)
print("Negative numbers:", negatives)
