"""
Exercise 5 – Dictionary of Students’ Ages
Create a dictionary named ages where keys are student names and values are their ages
(at least 4 students).
Then:
1. Ask the user to enter an age limit
2. Print the names of all students whose age is greater than or equal to that limit
3. If no student satisfies the condition, print "No student meets the age
requirement."
"""

ages = {"Alice": 20, "Bob": 18, "Charlie": 22, "Diana": 19}

try:
    age_limit = int(input("Enter an age limit: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()

filtered_students = [name for name, age in ages.items() if age >= age_limit]

if len(filtered_students) > 0:
    print("Students meeting the age requirement:")
    for name in filtered_students:
        print(name)
else:
    print("No student meets the age requirement.")
