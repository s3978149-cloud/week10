"""
Exercise 9 — CSV: Compute a New Column
Task: Given sales.csv with columns: item,price,quantity
Create sales_total.csv containing: item,price,quantity,total
where total = price * quantity.
Requirement: Keep header row and preserve item name
"""

import csv

try:
    with open("sales.csv", "r", newline="") as infile, open(
        "sales_total.csv", "w", newline=""
    ) as outfile:
        reader = csv.DictReader(infile)
        fieldnames = ["item", "price", "quantity", "total"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in reader:
            total = float(row["price"]) * int(row["quantity"])
            writer.writerow(
                {
                    "item": row["item"],
                    "price": row["price"],
                    "quantity": row["quantity"],
                    "total": total,
                }
            )

    print("Computed total column and wrote to sales_total.csv")
except FileNotFoundError:
    print("Error: sales.csv file not found.")
except ValueError:
    print("Error: Invalid numeric value found in sales.csv.")
except KeyError as e:
    print(f"Error: Missing expected column in CSV file: {e}")
except csv.Error as e:
    print(f"Error processing CSV file: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
