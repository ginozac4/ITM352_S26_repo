# Algorithm for multiplying two numbers by successive addition.

def multiply(x, y):
   product = x
   for i in range(y-1):
        product += x
  
   return product

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
prod = multiply(first, second)

print(f"The product of {first}, {second} is {prod}")