"""
Exercise 15 — Functions: Validate Numbers File
numbers.txt is supposed to contain one integer per line, but some lines may be invalid.
Write:
● is_valid_int(s) → returns True if s can be parsed as an integer
● split_valid_invalid(input_path, valid_out, invalid_out) → writes
valid integers to valid.txt and invalid lines to invalid.txt
In main, call split_valid_invalid(...) on numbers.txt.


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s
"""


def is_valid_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def split_valid_invalid(input_path, valid_out, invalid_out):
    try:
        with open(input_path, "r") as infile, open(valid_out, "w") as validfile, open(invalid_out, "w") as invalidfile:
            for line in infile:
                stripped_line = line.rstrip("\n")
                if is_valid_int(stripped_line):
                    validfile.write(stripped_line + "\n")
                else:
                    invalidfile.write(stripped_line + "\n")
    except FileNotFoundError:
        print(f"Error: {input_path} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


split_valid_invalid("numbers.txt", "valid.txt", "invalid.txt")
