"""
Exercise 10 – Pass / Fail Split from Grade Dictionary
Suppose you have a dictionary where:
● keys = student names
● values = their exam scores
Write a function
split_pass_fail(grades, pass_mark)
that returns two lists:
● first list: names of students with scores greater than or equal to pass_mark
● second list: names of students with scores less than pass_mark
In the main program:
1. Create a grades dictionary with at least 5 students
2. Ask the user to enter a pass_mark
3. Call the function
4. Print the list of passed students and the list of failed students in a clear forma
"""


def split_pass_fail(grades, pass_mark):
    passed = []
    failed = []
    for student, score in grades.items():
        if score >= pass_mark:
            passed.append(student)
        else:
            failed.append(student)
    return passed, failed


# Main program
grades = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eve": 78}
pass_mark = int(input("Enter the pass mark: "))
passed_students, failed_students = split_pass_fail(grades, pass_mark)
print("Passed students:", passed_students)
print("Failed students:", failed_students)
