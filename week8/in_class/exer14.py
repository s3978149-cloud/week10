"""
Exercise 14 — Count Occurrences
Write a function count_value(lst, value) that returns how many times value appears
in lst.
In main, create a list and ask the user for a value to count.
Call the function and print the result.
"""


def count_value(lst, value):
    count = 0
    for item in lst:
        if item == value:
            count += 1
    return count


numbers = [1, 2, 3, 2, 4, 2, 5]
value_to_count = int(input("Enter a value to count in the list: "))
occurrences = count_value(numbers, value_to_count)

# Alternative: using list.count() method
# occurrences = numbers.count(value_to_count)

print(f"The value {value_to_count} appears {occurrences} times in the list {numbers}.")
