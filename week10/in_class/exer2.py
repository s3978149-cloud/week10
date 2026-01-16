"""
Exercise 2 — Count Lines, Words, Characters (Text → Text Report)
Task: Read from input.txt. Compute:
1. number of lines
2. total number of words (split by spaces)
3. total number of characters (including spaces)
Write the results as a 3-line report to report.txt.
"""

try:
    with open("input.txt", "r") as infile:
        lines = infile.readlines()

    num_lines = len(lines)
    num_words = sum([len(line.strip().split()) for line in lines])
    num_characters = sum([len(line.replace("\n", "")) for line in lines])

    with open("report.txt", "w") as report_file:
        report_file.write(f"Number of lines: {num_lines}\n")
        report_file.write(f"Total number of words: {num_words}\n")
        report_file.write(f"Total number of characters: {num_characters}\n")

    print("Report written to report.txt")
except FileNotFoundError:
    print("Error: input.txt file not found.")
