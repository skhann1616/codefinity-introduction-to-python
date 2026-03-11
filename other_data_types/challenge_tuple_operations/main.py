# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# Task 1: Count how many apples are on the shelf
apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")

# Task 2: Find the index of the first occurrence of bananas
banana_index = shelf.index("bananas")
print(f"First Banana Index: {banana_index}")

# Task 3: Check if apples need to be restocked
if apple_count < 5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

# Task 4: Check if grapes need to be restocked (if grapes appear only once)
grape_count = shelf.count("grapes")
if grape_count == 1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

# Task 5: Check if oranges are on the shelf and print their index or stock status
if "oranges" in shelf:
    orange_index = shelf.index("oranges")
    print(f"Oranges are at index: {orange_index}")
else:
    print("Oranges are out of stock.")