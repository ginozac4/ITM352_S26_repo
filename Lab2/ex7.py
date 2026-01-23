#Ask user to enter a temperature in Farenheit.
#Convert Farenheit to Celsius using the formula C = (F - 32) * 5/9

'''
farenheit_input = input("Please enter temperature in Farenheit: ")
farenheit_value = float(farenheit_input)
celsius_value = (farenheit_value - 32) * 5/9
celsius_value_rounded = round(celsius_value, 2)

print("You entered:", farenheit_value)
print(f"The temperature in Celsius is: {celsius_value_rounded} °C")
'''

def temperature_conversion():
    farenheit_input = input("Please enter temperature in Farenheit: ")
    farenheit_value = float(farenheit_input)
    celsius_value = (farenheit_value - 32) * 5/9
    celsius_value_rounded = round(celsius_value, 2)

    print("You entered:", farenheit_value)
    print(f"The temperature in Celsius is: {celsius_value_rounded} °C")
temperature_conversion()