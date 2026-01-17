"""
Exercise 6 – Remove All Occurrences
Write a function
remove_value(lst, value)
that returns a new list containing all elements of lst except those equal to value.
In the main program:
1. Create a list of integers with some repeated values
2. Ask the user for a value to remove
3. Call remove_value and print the resulting list
"""


def remove_value(lst, value):
    return [item for item in lst if item != value]


# Main program
numbers = [1, 2, 3, 4, 2, 5, 2, 6]

value_to_remove = int(input("Enter a value to remove: "))

resulting_list = remove_value(numbers, value_to_remove)
print("Resulting list:", resulting_list)
