"""
Exercise 10 — Remove Items from a Dictionary
Given:
capitals = {"Vietnam": "Hanoi", "Japan": "Tokyo", "USA":
"Washington", "France": "Paris"}
Remove:
1. The entry for "Japan" using .pop()
2. The entry for "France" using del
Print the dictionary afterward.

"""

capitals = {
    "Vietnam": "Hanoi",
    "Japan": "Tokyo",
    "USA": "Washington",
    "France": "Paris",
}
# 1. Remove the entry for "Japan" using .pop()
capitals.pop("Japan")
# 2. Remove the entry for "France" using del
del capitals["France"]
print(capitals)  # Print the updated dictionary
