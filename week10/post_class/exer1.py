"""
Exercise 1 — Trim and Re-save
Input: raw.txt
Task: Create trimmed.txt where each line is stripped of leading/trailing spaces.
Requirements:
1. Keep the same number of lines as raw.txt
2. Do not remove empty lines; an empty line remains empty

Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s)
"""


def trim_and_resave(input_path, output_path):
    try:
        with open(input_path, "r") as infile, open(output_path, "w") as outfile:
            for line in infile:
                trimmed_line = line.strip()
                outfile.write(trimmed_line + "\n")
    except FileNotFoundError:
        print(f"Error: {input_path} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


trim_and_resave("raw.txt", "trimmed.txt")
