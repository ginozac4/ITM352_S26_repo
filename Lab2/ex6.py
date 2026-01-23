#Ask user to enter weight in pounds. Use float to convert.
# Convert pounds to kilograms (1 pound = 0.453592 kg) and print result.

'''
kg_to_pounds = 0.453592

weight_in_pounds = input("Please enter your weight in pounds: ")
weight_in_pounds_float = float(weight_in_pounds)
weight_in_kg = weight_in_pounds_float * kg_to_pounds
weight_in_kg_rounded = round(weight_in_kg, 2)

print(f"You entered: {weight_in_pounds} pounds")
print(f"Your weight in kilograms is: {weight_in_kg_rounded} kg") '''

print(float(input("Please enter your weight in pounds: ")) * 0.453592)