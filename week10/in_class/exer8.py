"""
Exercise 8 — CSV: Copy Selected Columns
Task: Given students.csv with columns: name,age,major,gpa
Write students_simple.csv containing only name and gpa columns.
Requirement: Keep the header row.
"""

import csv

try:
    with open("students.csv", "r", newline="") as infile, open(
        "students_simple.csv", "w", newline=""
    ) as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ["name", "gpa"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            writer.writerow({"name": row["name"], "gpa": row["gpa"]})

    print("Selected columns copied to students_simple.csv")
except FileNotFoundError:
    print("Error: students.csv file not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
except KeyError as e:
    print(f"Error: Missing expected column in CSV file: {e}")
except csv.Error as e:
    print(f"Error processing CSV file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
