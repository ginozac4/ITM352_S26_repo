#Name: Cassiddy Ginoza
#Date: Feb. 5, 2026

country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London"}

print(country_capitals)

print(country_capitals["Canada"])
print(country_capitals["England"])

country_capitals["Italy"] = "Rome"

print(country_capitals)
# with big data sets, might not be as efficient

country_capitals["Italy"] = "Milan"
print(country_capitals)

print("Germany" in country_capitals)
print("Spain" not in country_capitals)
print("Korea" in country_capitals)