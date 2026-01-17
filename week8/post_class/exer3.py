"""
Exercise 3 – Average Score from a List
Create a list named scores containing at least 5 integer scores.
Then:
1. Use a loop to compute the total sum of the scores
2. Compute the average as total / number_of_scores
3. Print both the total and the average
(Do not use built-in functions like sum().
"""

scores = [85, 90, 78, 92, 88]
total = 0
for score in scores:
    total += score
average = total / len(scores)
print("Total:", total)
print("Average:", average)
