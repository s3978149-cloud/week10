"""
Exercise 20 — Student Grades Report
Given a dictionary mapping student names to grades, write three functions:
1. average_grade(d) → returns the average grade
2. highest_grade(d) → returns the name and grade of the highest-scoring student
3. print_report(d) → prints:
○ Total students
○ Average grade
○ Student with the highest grade
In main, create a dictionary of at least 4 students, call all three functions, and display the full
report.
"""


def average_grade(d):
    total = sum(d.values())
    count = len(d)
    return total / count if count > 0 else 0


def highest_grade(d):
    if not d:
        return None, None
    highest_score = max(d.values())
    top_students = [student for student, grade in d.items() if grade == highest_score]
    return top_students, highest_score


def print_report(d):
    total_students = len(d)
    avg_grade = average_grade(d)
    highest_student, highest_score = highest_grade(d)
    print(f"Total students: {total_students}")
    print(f"Average grade: {avg_grade:.2f}")
    if highest_student is not None:
        print(f"Highest grade: {highest_student} with a score of {highest_score}")
    else:
        print("No students in the report.")


# Main program
students_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 90}
print_report(students_grades)
