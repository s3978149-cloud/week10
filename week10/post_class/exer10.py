"""
Exercise 10 — CSV: Add a Status Column
Input: scores.csv with columns student,score
Task: Create scores_with_status.csv with columns student,score,status where:
● status = PASS if score ≥ 50
● status = FAIL otherwise
Requirement: Keep the header row and original row order


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s)
"""

import csv


def add_status_column(input_csv, output_csv):
    try:
        with open(input_csv, "r", newline="") as infile, open(
            output_csv, "w", newline=""
        ) as outfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames + ["status"]
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                score = float(row["score"])
                row["status"] = "PASS" if score >= 50 else "FAIL"
                writer.writerow(row)
    except FileNotFoundError:
        print(f"Error: {input_csv} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


add_status_column("scores.csv", "scores_with_status.csv")
