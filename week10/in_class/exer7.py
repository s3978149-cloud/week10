"""
Exercise 7 — Filter Numbers by Threshold
Task: Ask the user for an integer threshold T.
Read from numbers.txt (one integer per line).
Write to filtered_numbers.txt only numbers greater than or equal to T.
Also write the count of kept numbers at the top of the output file.
"""

try:
    threshold = int(input("Enter the integer threshold T: "))

    kept_numbers = []
    with open("numbers.txt", "r") as infile:
        for line in infile:
            num = int(line.strip())
            if num >= threshold:
                kept_numbers.append(num)

    with open("filtered_numbers.txt", "w") as outfile:
        outfile.write(f"Count: {len(kept_numbers)}\n")
        for num in kept_numbers:
            outfile.write(f"{num}\n")

    print("Filtered numbers written to filtered_numbers.txt")
except FileNotFoundError:
    print("Error: numbers.txt file not found.")
except ValueError:
    print("Error: Non-integer value found in numbers.txt or invalid threshold input.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
