"""
Exercise 6 — Remove Elements
Given this list:
fruits = ["apple", "banana", "kiwi", "orange", "mango"]
Do the following:
1. Remove "banana" using .remove()
2. Remove the last element using .pop()
Print the updated list.
"""

fruits = ["apple", "banana", "kiwi", "orange", "mango"]
fruits.remove("banana")  # 1. Remove "banana" using .remove()
print(fruits)  # Print the list after removing "banana"
fruits.pop()  # 2. Remove the last element using .pop()
print(fruits)  # Print the updated list
