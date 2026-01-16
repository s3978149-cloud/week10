"""
Exercise 10 — CSV: Count Rows Matching a Condition
Task: Given students.csv with columns: name,age,major,gpa
Count how many students have gpa >= 3.0.
Write the result to gpa_report.txt as one line:
Number of students with GPA >= 3.0: <count>
"""

import csv

try:
    with open("students.csv", "r", newline="") as infile, open("gpa_report.txt", "w", newline=""    ) as outfile:
        reader = csv.DictReader(infile)
        count = 0
        for row in reader:
            if float(row["gpa"]) >= 3.0:
                count += 1

        outfile.write(f"Number of students with GPA >= 3.0: {count}\n")

    print("GPA report written to gpa_report.txt")
except FileNotFoundError:
    print("Error: students.csv file not found.")
except ValueError:
    print("Error: Invalid numeric value found in students.csv.")
except KeyError as e:
    print(f"Error: Missing expected column in CSV file: {e}")
except csv.Error as e:
    print(f"Error processing CSV file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
