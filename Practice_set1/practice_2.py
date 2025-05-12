#  Problem_3

# Assign a letter Grade based on the student's score. A (90-100)., B(80-89, c(70-79)), d(60-69), f(below 60)



grade = int(input("Enter Your Score to Calculate your Grade: "))

if grade >= 101:
    print("Please Enter a Valid Score")
    exit()

if grade >= 90:
    print("Congratulation You Got A")
elif grade > 89:
    print("Congratulation, you got B")
elif grade > 79:
    print("Congratulation, you got C")
elif grade > 69:
    print("Congratulation, you got D")
else: 
    print("Sorry, you got F. Better luck next time")