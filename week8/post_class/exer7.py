"""
Exercise 7 – All Elements Above a Threshold
Write a function
all_above(lst, threshold)
that returns True if all elements in lst are strictly greater than threshold, and False
otherwise.
In the main program:
1. Create a list of numbers
2. Ask the user for a threshold value
3. Call the function and print a message like:
○ "All values are above the threshold."
○ or "Some values are not above the threshold."
"""


def all_above(lst, threshold):
    for item in lst:
        if item <= threshold:
            return False
    return True


# Main program
numbers = [10, 20, 30, 40, 50]
threshold = float(input("Enter a threshold value: "))

if all_above(numbers, threshold):
    print("All values are above the threshold.")
else:
    print("Some values are not above the threshold.")
