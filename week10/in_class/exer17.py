"""
Exercise 17 — Functions: CSV Group Count
Given logs.csv with columns: user,action (one action per row).
Write:
● count_actions(input_csv) → returns a dictionary mapping action ->
count
● write_action_report(counts, output_path) → writes a text report sorted
by action name
In main, call the functions and produce action_report.txt.



Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s
"""

import csv


def count_actions(input_csv):
    action_counts = {}
    try:
        with open(input_csv, "r") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                action = row["action"]
                if action in action_counts:
                    action_counts[action] += 1
                else:
                    action_counts[action] = 1
    except FileNotFoundError:
        print(f"Error: {input_csv} file not found.")
        return None
    return action_counts


def write_action_report(counts, output_path):
    try:
        with open(output_path, "w") as outfile:
            for action in sorted(counts.keys()):
                outfile.write(f"{action}: {counts[action]}\n")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")


action_counts = count_actions("logs.csv")
if action_counts is not None:
    write_action_report(action_counts, "action_report.txt")
    print(f"Action report written to action_report.txt")
