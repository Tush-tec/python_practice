# Validate Input

# Keep Asking the User for Input Until they Enter a Number between 1 and 10

  
while True:
    number = int(input("Enter a Value b/w 1 to 10: "))
    if 1 <= number <=10:
        print("Thanks")
        break
    else :
        print("Invalid Input")