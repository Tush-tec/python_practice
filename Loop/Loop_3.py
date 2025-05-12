# Multiplication Table Printer

# Print the Multiplication Table For a Given Number up to 10, But SKip th 5th Iteration


number = 19

for i in range(1, 11):
    if i  == 5:
        continue  #  For Skip the iteration on conditional based.
    print(number, "x", i, "=", number * i)

 
