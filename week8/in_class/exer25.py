"""
Exercise 25 — Check If All Keys Present
Write a function
has_all_keys(d, required_keys)
where d is a dictionary and required_keys is a list of strings.
The function returns True if all required keys are present in the dictionary, and False
otherwise.
In main:
● Create a dictionary representing a student: name, age, major, maybe others.
● Create a list of required keys (e.g., ["name", "age", "major"]).
● Call the function and print whether the dictionary is “complete” or “incomplete”.

"""


def has_all_keys(d, required_keys):
    for key in required_keys:
        if key not in d:
            return False
    return True


# Main program
student = {"name": "John", "age": 20, "major": "Computer Science"}
required_keys = ["name", "age", "major"]
if has_all_keys(student, required_keys):
    print("The student dictionary is complete.")
else:
    print("The student dictionary is incomplete.")
