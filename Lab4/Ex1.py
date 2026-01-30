# string manipulation examples
# Name: Cassiddy Ginoza
# Date: Jan. 29, 2026

first = input("Enter your first name: ")
middleIn = input("Enter your middle initial: ")
last = input("Enter your last name: ")

full_name = first + " " + middleIn + ". " + last
print("Your full name is:", full_name)

print(f"Your full name is: {first} {middleIn}. {last}")

#use the percent operator method
print("Your full name is: %s %s. %s" % (first, middleIn, last))
#use the format method

print("Your full name is: {} {}. {}".format(first, middleIn, last))

#use the join method
print("Your full name is: " + " ".join([first, middleIn + ".", last]))

# use the format() method for a string and unpack the list as the argument
name_parts = [first, middleIn + ".", last]
print("Your full name is: {}".format(" ".join(name_parts)))