"""
Exercise 3 — Keep Only Non-Empty Lines
Task: Read from input.txt and write to clean.txt only the lines that are not empty after
stripping spaces.
"""

try:
    with open("input.txt", "r") as infile, open("clean.txt", "w") as outfile:
        for line in infile:
            if line.strip() != "":  # Check if the line is not empty after stripping spaces
                outfile.write(line)
    print("Non-empty lines written to clean.txt")
except FileNotFoundError:
    print("Error: input.txt file not found.")
