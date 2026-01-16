"""
Exercise 4 — Uppercase All Lines
Task: Read from input.txt. Write the lines to upper.txt where all letters are converted
to uppercase.
"""

try:
    with open("input.txt", "r") as infile, open("upper.txt", "w") as outfile:
        for line in infile:
            outfile.write(line.upper())
    print("All lines converted to uppercase and written to upper.txt")
except FileNotFoundError:
    print("Error: input.txt file not found.")
