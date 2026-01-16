"""
Exercise 4 — Find Top 3 Longest Lines
Input: input.txt
Task: Create top3_longest.txt containing the 3 longest lines from the file (by character
count).
Requirements:
1. Keep the original text of those lines
2. If ties occur, keep the earlier line first
3. Output exactly 3 lines (assume input has at least 3 lines


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s)
"""


def find_top3_longest(input_txt, output_txt):
    try:
        with open(input_txt, "r") as infile:
            lines = infile.readlines()
            # Sort lines by length (descending) while preserving original order for ties
            sorted_lines = sorted(enumerate(lines), key=lambda x: (-len(x[1]), x[0]))
            top3_lines = [line for index, line in sorted_lines[:3]]
        with open(output_txt, "w") as outfile:
            outfile.writelines(top3_lines)
    except FileNotFoundError:
        print(f"Error: {input_txt} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


find_top3_longest("input.txt", "top3_longest.txt")
