"""
Exercise 1 — Copy with Line Numbers (Text → Text)
Task: Read from input.txt, line by line. Write the line to output.txt where each line is
prefixed with its line number starting from 1.
Requirement: Keep the original line content (except adding the number).
"""

try:
    with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
        for line_number, line_content in enumerate(infile, start=1):
            outfile.write(f"{line_number} {line_content}")
    print("Lines copied with line numbers to output.txt")
except FileNotFoundError:
    print("Error: input.txt file not found.")
