"""
Exercise 12 — Function: Longest Line Finder
Write a function longest_line(input_path) that returns:
● the longest line (without trailing newline)
● its line number (starting from 1)
In main, call it on input.txt and write a report to longest_line.txt.
Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s
"""


def longest_line(input_path):
    max_length = 0
    longest = ""
    line_number = 0
    try:
        with open(input_path, "r") as infile:
            for idx, line in enumerate(infile, start=1):
                line_content = line.rstrip("\n")
                if len(line_content) > max_length:
                    max_length = len(line_content)
                    longest = line_content
                    line_number = idx
    except FileNotFoundError:
        print(f"Error: {input_path} file not found.")
        return None, None
    return longest, line_number


longest, line_number = longest_line("input.txt")
if longest is not None:
    try:
        with open("longest_line.txt", "w") as outfile:
            outfile.write(f"The longest line is on line {line_number}:\n")
            outfile.write(longest + "\n")
        print(f"Longest line report written to longest_line.txt")
    except Exception as e:
        print(f"Error writing to longest_line.txt: {e}")
