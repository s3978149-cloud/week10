"""
Exercise 14 — Function: Merge Two Text Files Alternating Lines
Write a function merge_alternating(file1, file2, out_file) that writes:
● line 1 of file1, line 1 of file2, line 2 of file1, line 2 of file2, ...
In main, call it to merge a.txt and b.txt into merged.txt.
Requirement: If one file ends early, append the remaining lines of the other file

Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s
"""


def merge_alternating(file1, file2, out_file):
    try:
        with open(file1, "r") as f1, open(file2, "r") as f2, open(out_file, "w") as out:
            lines1 = f1.readlines()
            lines2 = f2.readlines()
            max_length = max(len(lines1), len(lines2))
            for i in range(max_length):
                if i < len(lines1):
                    out.write(lines1[i])
                if i < len(lines2):
                    out.write(lines2[i])
    except FileNotFoundError as e:
        print(f"Error: {e.filename} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


merge_alternating("a.txt", "b.txt", "merged.txt")
