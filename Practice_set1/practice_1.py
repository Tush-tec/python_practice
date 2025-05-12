# Age Group Categorisation

#  Classify A Person age group : Child ( < 13), Teenager (13-19), Young Adult (20-39), Adult (40-64),

age = int(input("Please Give me Your Age to Classify Your Age Group: "))


if age < 13:
    print("You're as Child")
elif age < 20:
    print("You're a Teenager")
elif age < 40:
    print("You're a Young Adult")
elif age < 60: 
    print("You're a Adult")
else:
    print("You're a Senior")



# Movie Ticker Pricing Classify

# Problem: Movie Tickets are priced based on age : $12 for Adults, $8 for Children. Everyone get a $2% discount on Wednesday.

age  = int(input("Enter Your Age : "))
day = input("Enter the Day of the Week : ")


price = 12 if age >= 18 else 8

if day  == "wednesday":
    price = price -  2
    print(f" You Got $2 discount & Your Movie Ticket Price is ${price}")
else:
    print(f"Your Movie Ticket Price is ${price}")
