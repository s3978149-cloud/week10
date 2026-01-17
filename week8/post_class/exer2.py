"""
Exercise 2 – Filter City Names by First Letter
Create a list named cities with at least 7 city names.
Then:
1. Ask the user to enter a letter (for example: H)
2. Print all city names in the list that start with that letter
3. If no city starts with that letter, print a message like:
No city starts with H.
"""

cities = [
    "Hanoi",
    "Helsinki",
    "Stockholm",
    "Copenhagen",
    "Oslo",
    "Osaka",
    "Reykjavik",
    "Amsterdam",
    "Berlin",
    "Brussels",
]
letter = input("Enter a letter: ").strip()
matching_cities = [city for city in cities if city.startswith(letter)]
if matching_cities:
    for city in matching_cities:
        print(city)
else:
    print(f"No city starts with {letter}.")
