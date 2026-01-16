"""
Exercise 9 — CSV: Find Maximum Amount Row
Input: transactions.csv with columns date,category,amount
Task: Create max_transaction.txt containing exactly one line describing the row with
the largest amount.
Requirements:
1. Output format: date=<...>, category=<...>, amount=<...>
2. If there is a tie, choose the earliest row in the file


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s)
"""

import csv


def find_max_transaction(input_csv, output_txt):
    max_row = None
    try:
        with open(input_csv, "r") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                try:
                    amount = float(row["amount"])
                except ValueError:
                    continue  # Skip rows with invalid amount
                if max_row is None or amount > float(max_row["amount"]):
                    max_row = row
        if max_row:
            with open(output_txt, "w") as outfile:
                outfile.write(
                    f"date={max_row['date']}, category={max_row['category']}, amount={max_row['amount']}\n"
                )
        else:
            print("No valid transactions found.")
    except FileNotFoundError:
        print(f"Error: {input_csv} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


find_max_transaction("transactions.csv", "max_transaction.txt")
