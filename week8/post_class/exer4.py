"""
Exercise 4 – Basic Product Dictionary
Create a dictionary named product with the following keys:
● "name" → product name
● "price" → product price
● "quantity" → product quantity in stock
Then:
1. Print all keys and their values
2. Update the "quantity" to a new value
3. Add a new key "category" with some value
4. Print the updated dictionar
"""

# Step 1: Create the product dictionary
product = {
    "name": "Laptop",
    "price": 1200.00,
    "quantity": 10,
}
# Step 2: Print all keys and their values
for key, value in product.items():
    print(f"{key}: {value}")
# Step 3: Update the "quantity" to a new value
product["quantity"] = 15
# Step 4: Add a new key "category" with some value
product["category"] = "Electronics"
# Step 5: Print the updated dictionary
print("\nUpdated product dictionary:")
for key, value in product.items():
    print(f"{key}: {value}")
