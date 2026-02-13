#determine movie price. 
# Name: Cassiddy Ginoza
# Date: Feb. 12, 2026

age = 60
weekday = "Wednesday"
matinee = True

price = 14

if age >= 65:
    price = min(price, 8)

if weekday == "Tuesday":
    price = min(price, 10)

if matinee:
    if age >= 65:
        price = min(price, 5)
    else:
        price = min(price, 8)

print("Age:", age)
print("Weekday:", weekday)
print("Matinee:", matinee)
print("Final Price: $", price)
