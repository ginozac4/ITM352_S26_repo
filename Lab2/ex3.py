# Ask the user to enter a floating point number. Square the number.
#Print out the original number and the squared result.

input_value = input("Enter a floating point number: ")
float_value = float(input_value)
squared_value = float_value ** 2

#round the number to 2 decimal places
squared_value = round(squared_value, 2)

print(f"You entered: {float_value}")
print(f"The squared result is: {squared_value}")
