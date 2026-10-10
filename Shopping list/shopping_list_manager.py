filename = "shopping_list.txt"

# Step 1: Create a text file and write an initial shopping list into it
initial_items = ["Apples", "Milk", "Bread", "Eggs"]

print("1. Creating shopping list and writing initial items...")
with open(filename, "w") as file:
    for item in initial_items:
        file.write(item + "\n")

# Step 2: Read and display the complete file content
print("\n2. Reading complete file content:")
with open(filename, "r") as file:
    content = file.read()
    print(content)

# Step 3: Append new items to the existing list
new_items = ["Butter", "Coffee Beans"]

print("3. Appending new items to the shopping list...")
with open(filename, "a") as file:
    for item in new_items:
        file.write(item + "\n")

# Step 4: Read the updated file line by line
print("\n4. Reading updated shopping list line by line:")
with open(filename, "r") as file:
    line_number = 1
    for line in file:
        print(f"  Item {line_number}: {line.strip()}")
        line_number += 1