# List uniqueness checker

# Check if all elements in a list are unique. if a duplicate is fount, exit the loop and print the duplicate.


items = ["apple", "mango", "banana", "apple", "orange"]
unique_items = set()

for item in items:
    if item in unique_items:
        print(f"Duplicate found: {item}")
        break
    else:
        unique_items.add(item)
        print("All items are unique")
        
print("All items are unique") 
