"""
Exercise 8 – Index of the Minimum Element
Write a function
index_of_min(lst)
that returns the index of the smallest element in lst.
If the smallest value appears multiple times, return the index of its first occurrence.
In the main program:
1. Create a list of numbers
2. Call the function
3. Print the smallest value and its index
Example output format:
The smallest value is 3 at index 2.
"""
def index_of_min(lst):
    if not lst:
        return None  # Handle empty list case
    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i
    return min_index
# Main program
numbers = [34, 12, 5, 67, 5, 89, 23]
min_index = index_of_min(numbers)
if min_index is not None:
    print(f"The smallest value is {numbers[min_index]} at index {min_index}.")
else:
    print("The list is empty.") 
    