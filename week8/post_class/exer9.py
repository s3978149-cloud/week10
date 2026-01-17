"""
Exercise 9 – Filter Dictionary by Key Prefix
Write a function
filter_by_prefix(d, prefix)
that takes a dictionary d and a string prefix, and returns a new dictionary containing only
those key–value pairs where the key starts with prefix.
In the main program:
1. Create a dictionary of usernames and IDs, for example:
○ "user1": 101, "user2": 102, "admin": 999, "user_test": 200,
etc.
2. Ask the user for a prefix (for example: "user")
3. Call the function and print the filtered dictionary
"""


def filter_by_prefix(d, prefix):
    return {key: value for key, value in d.items() if key.startswith(prefix)}


# Main program
user_dict = {"user1": 101, "user2": 102, "admin": 999, "user_test": 200, "guest": 300}
prefix = input("Enter a prefix to filter by: ")
filtered_dict = filter_by_prefix(user_dict, prefix)
print("Filtered dictionary:", filtered_dict)
