import csv

# question 1
def largest_power_of_5(n):
    power = 1 

    while power * 5 < n:
        power *= 5  

    return power

print("Input of n: ")
n = int(input())  
print(largest_power_of_5(n))

# question 2
def email_search(input_file, output_file, email):
    with open(input_file, "r") as fin, open(output_file, "w") as fout:
        for line in fin:
            line = line.strip()  # remove newline
            if email in line:  # check substring
                fout.write(line + "\n")  # write matching line


email = input("Enter email address: ")
email_search("question2.txt", "output.txt", email)

# question 3
def most_profitable_product(category):
    max_profit = -1  
    best_product = ""  

    with open("sales.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["category"] == category:
                profit = int(row["profit"])  # convert profit to int
                if profit > max_profit:
                    max_profit = profit
                    best_product = row["product_id"]

    return best_product


print(most_profitable_product("Electronics"))  
print(most_profitable_product("Books"))  

# question 4
def best_seller(sales):
    num_products = len(sales[0]) 
    totals = [0] * num_products  

    # sum sales of product
    for day in sales:
        for i in range(num_products):
            totals[i] += day[i]

    # find idx of max total
    best_index = 0
    for i in range(1, num_products):
        if totals[i] > totals[best_index]:
            best_index = i

    return best_index


print(best_seller([[10, 20, 15], [15, 20, 35], [20, 25, 15], [9, 30, 35]]))
print(best_seller([[15,30,10], [15,19,30], [20,15,15]]))

# question 5
def next_word(word):
    counts = {}  # dict to count next words

    # read file line by line
    with open("question5.txt", "r") as file:
        for line in file:
            words = line.strip().split()  # split sentence into word

            # check word except the last 
            for i in range(len(words) - 1):
                if words[i] == word:
                    next_w = words[i + 1]  # word after input word
                    counts[next_w] = counts.get(next_w, 0) + 1

    if not counts:
        return []

    # find most frequency
    max_count = max(counts.values())

    # get words with highest frequency
    result = []
    for w in counts:
        if counts[w] == max_count:
            result.append(w)

    return result


print(next_word("I"))  
print(next_word("like"))  
