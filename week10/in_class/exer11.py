"""
Exercise 11 — Function: Count Keyword Occurrences (Text)
Write a function count_keyword_in_file(input_path, keyword) that returns how
many lines contain the keyword.
In main:
1. ask the user for keyword
2. call the function on input.txt
3. write the count to keyword_count.txt

Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s
"""


def count_keyword_in_file(input_path, keyword):
    count = 0
    try:
        with open(input_path, "r") as infile:
            for line in infile:
                if keyword in line:
                    count += 1
    except FileNotFoundError:
        print(f"Error: {input_path} file not found.")
        return None
    return count


keyword = input("Enter the keyword to search for: ")
count = count_keyword_in_file("input.txt", keyword)
if count is not None:
    try:
        with open("keyword_count.txt", "w") as outfile:
            outfile.write(f"The keyword '{keyword}' was found in {count} lines.\n")
        print(f"Keyword count written to keyword_count.txt")
    except Exception as e:
        print(f"Error writing to keyword_count.txt: {e}")
