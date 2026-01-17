"""
Exercise 1 – Build a List from User Input
Ask the user to enter 5 integers, one by one.
For each input, append the number to a list named numbers.
After that:
1. Print the final list
2. Print the smallest number using min()
3. Print the largest number using max()

"""

numbers = []
for _ in range(5):
    num = int(input("Enter an integer: "))
    numbers.append(num)

print("Final list:", numbers)
print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))
