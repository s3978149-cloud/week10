"""
Exercise 18 — Functions: CSV Compute Average per Group
Given scores.csv with columns: student,subject,score
Write:
● average_score_per_subject(input_csv) → returns a dictionary subject
-> average_score
● write_subject_averages(avg_dict, output_path) → writes results to
subject_averages.txt
In main, call them and create the report.




Additional requirements:
✅ Write one or more functions
✅ Call them from the main program
✅ Read from file(s) and write output file(s
"""

import csv


def average_score_per_subject(input_csv):
    subject_totals = {}
    subject_counts = {}
    try:
        with open(input_csv, "r") as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                subject = row["subject"]
                try:
                    score = float(row["score"])
                except ValueError:
                    continue  # Skip invalid score entries
                if subject in subject_totals:
                    subject_totals[subject] += score
                    subject_counts[subject] += 1
                else:
                    subject_totals[subject] = score
                    subject_counts[subject] = 1
    except FileNotFoundError:
        print(f"Error: {input_csv} file not found.")
        return None
    avg_dict = {
        subject: subject_totals[subject] / subject_counts[subject]
        for subject in subject_totals
    }
    return avg_dict

"""_sum
"""
import csv


def most_profitable_product(category):
    max_profit = -1  # highest profit found
    best_product = ""  # product id with highest profit

    with open("sales.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["category"] == category:
                profit = int(row["profit"])  # convert profit to int
                if profit > max_profit:
                    max_profit = profit
                    best_product = row["product_id"]

    return best_product


print(most_profitable_product("Electronics"))  # expected P003
print(most_profitable_product("Books"))  # expected P008


"""_sum
"""

def write_subject_averages(avg_dict, output_path):
    try:
        with open(output_path, "w") as outfile:
            for subject in sorted(avg_dict.keys()):
                outfile.write(f"{subject}: {avg_dict[subject]:.2f}\n")
    except Exception as e:
        print(f"Error writing to {output_path}: {e}")


avg_dict = average_score_per_subject("scores.csv")
if avg_dict is not None:
    write_subject_averages(avg_dict, "subject_averages.txt")
    print("Subject averages written to subject_averages.txt")
