"""
Exercise 20 — Mini Project: Clean + Summarize CSV
Given transactions.csv with columns: date,category,amount
Some rows may have:
● missing category
● invalid amount (not a number)
Write these functions:
1. is_valid_amount(s) → checks whether s is a valid number
2. clean_transactions(input_csv, clean_csv, bad_rows_txt) → writes
valid rows to clean_transactions.csv, invalid rows to bad_rows.txt
3. sum_by_category(clean_csv) → returns dictionary category ->
total_amount
4. write_category_summary(summary, out_txt) → writes a neat summary
report
In main:
● call cleaning
● then compute totals per category
● output category_summary.txt


Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s)
"""

import csv


def is_valid_amount(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def clean_transactions(input_csv, clean_csv, bad_rows_txt):
    try:
        with open(input_csv, "r") as infile, open(
            clean_csv, "w", newline=""
        ) as cleanfile, open(bad_rows_txt, "w") as badfile:
            reader = csv.DictReader(infile)
            fieldnames = reader.fieldnames
            writer = csv.DictWriter(cleanfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in reader:
                if row["category"].strip() == "" or not is_valid_amount(row["amount"]):
                    badfile.write(f"{row}\n")
                else:
                    writer.writerow(row)
    except FileNotFoundError:
        print(f"Error: {input_csv} file not found.")
    except Exception as e:
        print(f"Error processing files: {e}")


"""_sum
"""
def next_word(word):
    counts = {}  # dictionary to count next words

    # read file line by line
    with open("input.txt", "r") as file:
        for line in file:
            words = line.strip().split()  # split sentence into words

            # check each word except the last one
            for i in range(len(words) - 1):
                if words[i] == word:
                    next_w = words[i + 1]  # word after input word
                    counts[next_w] = counts.get(next_w, 0) + 1

    if not counts:
        return []

    # find highest frequency
    max_count = max(counts.values())

    # collect all words with highest frequency
    result = []
    for w in counts:
        if counts[w] == max_count:
            result.append(w)

    return result


print(next_word("I"))  # expected ['like']
print(next_word("like"))  # expected ['apples', 'bananas']


"""_sum
"""

def sum_by_category(clean_csv):
    category_totals = {}
    try:
        with open(clean_csv, "r") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                category = row["category"]
                amount = float(row["amount"])
                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount
    except FileNotFoundError:
        print(f"Error: {clean_csv} file not found.")
        return None
    return category_totals


def write_category_summary(summary, out_txt):
    try:
        with open(out_txt, "w") as outfile:
            for category in sorted(summary.keys()):
                outfile.write(f"{category}: {summary[category]:.2f}\n")
    except Exception as e:
        print(f"Error writing to {out_txt}: {e}")


clean_transactions("transactions.csv", "clean_transactions.csv", "bad_rows.txt")
summary = sum_by_category("clean_transactions.csv")
if summary is not None:
    write_category_summary(summary, "category_summary.txt")
    print("Category summary written to category_summary.txt")
