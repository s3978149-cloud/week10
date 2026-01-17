"""
Exercise 19 — Functions: Detect Duplicate IDs in CSV
Given employees.csv with columns: id,name,department
Write:
● find_duplicate_ids(input_csv) → returns a set (or list) of IDs that appear
more than once
● write_duplicates(duplicates, output_path) → writes them to
duplicate_ids.txt, one per line
In main, call the functions and write the report.


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s
"""

import csv


def find_duplicate_ids(input_csv):
    id_counts = {}
    try:
        with open(input_csv, "r") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                emp_id = row["id"]
                if emp_id in id_counts:
                    id_counts[emp_id] += 1
                else:
                    id_counts[emp_id] = 1
    except FileNotFoundError:
        print(f"Error: {input_csv} file not found.")
        return None
    duplicates = {emp_id for emp_id, count in id_counts.items() if count > 1}
    return duplicates


"""_sum
"""
def best_seller(sales):
    num_products = len(sales[0])  # number of columns
    totals = [0] * num_products  # total sales per product

    # sum sales for each product
    for day in sales:
        for i in range(num_products):
            totals[i] += day[i]

    # find index of highest total
    best_index = 0
    for i in range(1, num_products):
        if totals[i] > totals[best_index]:
            best_index = i

    return best_index


sales_data = [[10, 20, 15], [15, 20, 35], [20, 25, 15], [9, 30, 35]]

print(best_seller(sales_data))  # expected 2


"""_sum
"""

def write_duplicates(duplicates, output_path):
    try:
        with open(output_path, "w") as outfile:
            for emp_id in sorted(duplicates):
                outfile.write(f"{emp_id}\n")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")


duplicates = find_duplicate_ids("employees.csv")
if duplicates is not None:
    write_duplicates(duplicates, "duplicate_ids.txt")
    print("Duplicate IDs written to duplicate_ids.txt")
