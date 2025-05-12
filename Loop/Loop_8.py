# Prime Number
# A prime number is a natural number greater than 1 that has no positive divisors other than.

# Check if number is prime


number = int(input("Enter a number: "))

is_prime = True

if number > 1:
    for i in range(2, number):
         if (number % i) == 0:
              is_prime = False
              break
         else:
              is_prime = True
             
print(is_prime)