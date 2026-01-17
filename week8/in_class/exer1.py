"""
Exercise 1 — Create and Print a List
Create a list named numbers containing exactly these integers: 5, 10, 15, 20, 25.
Print the entire list and print its length.

"""

numbers = [5, 10, 15, 20, 25]
for num in numbers:
    print(num)

# Alternative using index:
# for index in range(len(numbers)):
#     print(f"numbers[{index}] = {numbers[index]}")

print("Length of the list:", len(numbers))
