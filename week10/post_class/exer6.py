"""
Exercise 6 — CSV: Select + Rename Columns
Input: students.csv with columns name,age,major,gpa
Task: Create students_export.csv containing only name,gpa but with headers
renamed to:
student_name,final_gpa
Requirement: Keep row order unchanged.


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s)
"""

import csv


def select_and_rename_columns(input_csv, output_csv):
    try:
        with open(input_csv, "r", newline="") as infile, open(
            output_csv, "w", newline=""
        ) as outfile:
            reader = csv.DictReader(infile)
            fieldnames = ["student_name", "final_gpa"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                writer.writerow({"student_name": row["name"], "final_gpa": row["gpa"]})
    except FileNotFoundError:
        print(f"Error: {input_csv} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


select_and_rename_columns("students.csv", "students_export.csv")
