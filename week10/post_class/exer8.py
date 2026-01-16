"""
Exercise 8 — CSV: Count Per Category
Input: transactions.csv with columns date,category,amount
Task: Create category_counts.txt showing how many rows belong to each category.
Requirements:
1. Output format: category: count (one per line)
2. Categories should be listed in alphabetical order


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s)
"""

import csv


def count_by_category(input_csv, output_txt):
    category_counts = {}
    try:
        with open(input_csv, "r") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                category = row["category"].strip()
                if category:
                    category_counts[category] = category_counts.get(category, 0) + 1
        with open(output_txt, "w") as outfile:
            for category in sorted(category_counts):
                outfile.write(f"{category}: {category_counts[category]}\n")
    except FileNotFoundError:
        print(f"Error: {input_csv} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


count_by_category("transactions.csv", "category_counts.txt")
