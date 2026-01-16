"""
Exercise 19 — Functions: Detect Duplicate IDs in CSV
Given employees.csv with columns: id,name,department
Write:
● find_duplicate_ids(input_csv) → returns a set (or list) of IDs that appear
more than once
● write_duplicates(duplicates, output_path) → writes them to
duplicate_ids.txt, one per line
In main, call the functions and write the report.


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s
"""

import csv


def find_duplicate_ids(input_csv):
    id_counts = {}
    try:
        with open(input_csv, "r") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                emp_id = row["id"]
                if emp_id in id_counts:
                    id_counts[emp_id] += 1
                else:
                    id_counts[emp_id] = 1
    except FileNotFoundError:
        print(f"Error: {input_csv} file not found.")
        return None
    duplicates = {emp_id for emp_id, count in id_counts.items() if count > 1}
    return duplicates


def write_duplicates(duplicates, output_path):
    try:
        with open(output_path, "w") as outfile:
            for emp_id in sorted(duplicates):
                outfile.write(f"{emp_id}\n")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")


duplicates = find_duplicate_ids("employees.csv")
if duplicates is not None:
    write_duplicates(duplicates, "duplicate_ids.txt")
    print("Duplicate IDs written to duplicate_ids.txt")
