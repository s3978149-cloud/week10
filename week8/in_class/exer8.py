"""
Exercise 8 — Create a Dictionary
Create a dictionary named student containing:
● "name" → your name
● "age" → your age
● "major" → your major
Print each key and its value on a separate line.

"""

student = {"name": "John Doe", "age": 21, "major": "Computer Science"}
for key, value in student.items():
    print(f"{key}: {value}")

# Alternative using keys:
# for key in student:
#     print(f"{key}: {student[key]}")
