"""
Exercise 7 — CSV: Filter by Exact Match
Input: students.csv with columns name,age,major,gpa
Task: Ask the user for a major (e.g., CS). Create major_filtered.csv containing only
students whose major matches exactly.
Requirement: Keep the header row


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s)
"""

import csv


def filter_by_major(input_csv, output_csv, major_filter):
    try:
        with open(input_csv, "r", newline="") as infile, open(
            output_csv, "w", newline=""
        ) as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                if row["major"] == major_filter:
                    writer.writerow(row)
    except FileNotFoundError:
        print(f"Error: {input_csv} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


major = input("Enter the major to filter by (e.g., CS): ")
filter_by_major("students.csv", "major_filtered.csv", major)
