"""
Exercise 13 — Functions: Normalize Whitespace
Write:
● normalize_line(line) → replaces multiple spaces with a single space and
strips leading/trailing spaces
● normalize_file(input_path, output_path) → reads input file and writes
normalized lines
In main, call normalize_file("input.txt", "normalized.txt").

Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s
"""

import re


def normalize_line(line):
    # Split the line into words and join with a single space, then strip
    normalized = " ".join(line.split())
    return normalized


def normalize_file(input_path, output_path):
    try:
        with open(input_path, "r") as infile, open(output_path, "w") as outfile:
            for line in infile:
                normalized_line = normalize_line(line)
                outfile.write(normalized_line + "\n")
    except FileNotFoundError:
        print(f"Error: {input_path} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


normalize_file("input.txt", "normalized.txt")
