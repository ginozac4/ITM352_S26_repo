# Name: Cassiddy Ginoza
# Date: Jan. 29, 2026

'''import HandyMath as HM

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
                
mid = HM.midpoint(number1, number2)
print(f"The midpoint between {number1} and {number2} is {mid}")

exp = HM.exponent(number1, number2, 2)
# if you put another number in the third comma, it will rewrite the default precision of 2
print(f"{number1} raised to the power of {number2} is {exp}")

max_value = HM.max(number1, number2)
print(f"The maximum between {number1} and {number2} is {max_value}")

min_value = HM.min(number1, number2)
print(f"The minimum between {number1} and {number2} is {min_value}") 

sqrt1 = HM.sqrt(number1)
print(f"The square root of {number1} is {sqrt1}")'''

'''from HandyMath import max, min
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: ")) 
max_value = max(number1, number2)
print(f"The maximum between {number1} and {number2} is {max_value}")
min_value = min(number1, number2)
print(f"The minimum between {number1} and {number2} is {min_value}")'''

from HandyMath import apply_function, max, min, midpoint, exponent

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
print(apply_function(number1, number2, max))
print(apply_function(number1, number2, min))
print(apply_function(number1, number2, exponent))  
