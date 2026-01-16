"""
Exercise 6 — Sum Numbers from a Text File
Task: Read from numbers.txt, where each line contains one integer.
Compute the total sum and write it to sum.txt as:
Total: <sum>
"""

try:
    total_sum = 0
    with open("numbers.txt", "r") as infile:
        for line in infile:
            total_sum += int(line.strip())

    with open("sum.txt", "w") as outfile:
        outfile.write(f"Total: {total_sum}\n")

    print("Total sum written to sum.txt")
except FileNotFoundError:
    print("Error: numbers.txt file not found.")
except ValueError:
    print("Error: Non-integer value found in numbers.txt.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
