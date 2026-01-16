"""
Exercise 16 — Function: CSV Filter by Column Condition
Write a function filter_csv_by_min_value(input_csv, output_csv,
column_name, min_value) that keeps only rows where the numeric column
column_name >= min_value.
In main:
1. ask user for min_value
2. call the function on students.csv for column gpa
3. write results to students_gpa_filtered.csv



Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s
"""
import csv
def filter_csv_by_min_value(input_csv, output_csv, column_name, min_value):
    try:
        with open(input_csv, mode='r', newline='') as infile, open(output_csv, mode='w', newline='') as outfile:
            reader = csv.DictReader(infile)
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
            writer.writeheader()
            for row in reader:
                try:
                    if float(row[column_name]) >= min_value:
                        writer.writerow(row)
                except ValueError:
                    print(f"Warning: Non-numeric value '{row[column_name]}' in column '{column_name}'. Skipping row.")
    except FileNotFoundError:
        print(f"Error: {input_csv} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")

"""_sum
    """


def most_similar_suffix(query):
    # Read strings from file
    with open("strings.txt", "r") as file:
        strings = [line.strip() for line in file]

    max_length = 0
    result = []

    for s in strings:
        # Find common suffix length
        i = 1
        while i <= min(len(s), len(query)) and s[-i] == query[-i]:
            i += 1

        common_length = i - 1

        # Update result list
        if common_length > max_length:
            max_length = common_length
            result = [s]
        elif common_length == max_length and common_length > 0:
            result.append(s)

    return result


# Main body
print(most_similar_suffix("talking"))


"""_sum
"""
try:
    min_value = float(input("Enter the minimum GPA value: "))
    filter_csv_by_min_value("students.csv", "students_gpa_filtered.csv", "gpa", min_value)
except ValueError:
    print("Invalid input. Please enter a numeric value for the minimum GPA.")
