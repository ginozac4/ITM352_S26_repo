# Name: Cassiddy Ginoza
# Date: Feb. 19, 2026

'''data = ("hello", 10, "goodbye", 3, "goodnight", 5, 6.7, True)

user_input = input("Enter a value to add to the tuple: ")

try:
    data.append(user_input)
except AttributeError as e:
    print(f"Error: You attempted to append a value to a tuple, which is not allowed.")
    print(f"Actual error message: {e}")'''

'''data = ("hello", 10, "goodbye", 3, "goodnight", 5, 6.7, True)

user_input = input("Enter a value to add to the tuple: ")

try:
    data.append(user_input)
except AttributeError:
    print("Attempting to append to a tuple... But tuples are immutable!")
    data = data + (user_input,)

print("Updated tuple:", data)'''

'''data = ("hello", 10, "goodbye", 3, "goodnight", 5, 6.7, True)

user_input = input("Enter a value to add to the tuple: ")

data = (*data, user_input)

print("Updated tuple:", data)'''

data = ("hello", 10, "goodbye", 3, "goodnight", 5, 6.7, True)
user_input = input("Enter a value to add to the tuple: ")

data_list = list(data)
data_list.append(user_input)  
data = tuple(data_list)  

print("Updated tuple:", data)