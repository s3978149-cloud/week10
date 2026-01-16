"""
Exercise 5 — Running Total (Numbers File)
Input: numbers.txt (one integer per line)
Task: Create running_total.txt where each line is the cumulative sum up to that line.
Example idea: if input is 2, 5, -1 then output lines are 2, 7, 6.


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s)
"""


def compute_running_total(input_txt, output_txt):
    try:
        with open(input_txt, "r") as infile, open(output_txt, "w") as outfile:
            running_total = 0
            for line in infile:
                try:
                    number = int(line.strip())
                    running_total += number
                    outfile.write(f"{running_total}\n")
                except ValueError:
                    print(f"Warning: Skipping invalid line '{line.strip()}'")
    except FileNotFoundError:
        print(f"Error: {input_txt} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


compute_running_total("numbers.txt", "running_total.txt")
