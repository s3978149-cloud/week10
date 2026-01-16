"""
Exercise 5 — Extract Lines Containing a Keyword
Task: Ask the user for a keyword in the main program.
Read from input.txt and write to matches.txt only the lines that contain the keyword
(case-sensitive)
"""

try:
    keyword = input("Enter the keyword to search for: ")

    with open("input.txt", "r") as infile, open("matches.txt", "w") as outfile:
        for line in infile:
            if keyword in line:
                outfile.write(line)
    print(f"Lines containing the keyword '{keyword}' have been written to matches.txt")
except FileNotFoundError:
    print("Error: input.txt file not found.")
