# This program demonstrates variable scope in Python.
# Name: Cassiddy Ginoza
# Date: Jan. 27, 2026

'''def calculate_discounted_price(price):
    global discount #doing this allows you to access the variable outside the function
    discount = 0.9
    price = price * discount
    print(f"Inside function, discounted price: {price:.2f}")
    return price
#functions start with a def, ends when you return a value'''

def calculate_discounted_price(price, discount):
    price = price * discount
    print(f"Inside function, discounted price: {price:.2f}")
    return price

discount = 0.6
price = 100 #not the same as the price in the function
print(f"Original price before function call: {price:.2f}")
discounted_price = calculate_discounted_price(price, discount)

print(f"Original price after function call: {price:.2f}")
print("Discount=", discount)
    #prints global discount variable because overrides the 0.6
    #don't want to use global since confusing.