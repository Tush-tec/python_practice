# Find the First Non-Repeated Character

input_str = input("Enter String value:")


for char in input_str:
    if input_str.count(char) == 1:
        print(f"The first non-repeated character is: {char}")
        break
    else:
        continue
    