#converts the input into a float and then rounds it to the nearest whole number
change = int(round(float(input("Enter amount of change needed to make: ")) * 100))

#asssigning the value to the types of coins
quarters = 25 
dimes = 10
nickels = 5
pennies = 1

#number of coins needed
num_quarters = 0
num_dimes = 0
num_nickels = 0
num_pennies = 0

while change > 0:
    if change >= quarters:
        #checking to see if change is greater than quarters
        change -= quarters
        #subtracting the value of quarters from change
        num_quarters += 1
        #adding the number of quarters needed by 1
    elif change >= dimes:
        change -= dimes
        num_dimes += 1
    elif change >= nickels:
        change -= nickels
        num_nickels += 1
    elif change >= pennies:
        change -= pennies
        num_pennies += 1

#printing amount of counted coins needed to create the change
print(f'num_quarters: {num_quarters}')
print(f'num_dimes: {num_dimes}')
print(f'num_nickels: {num_nickels}')
print(f'num_pennies: {num_pennies}')