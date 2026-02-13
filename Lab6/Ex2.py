# Name: Cassiddy Ginoza
# Date: Feb. 10, 2026

test_cases = [
    [1, 2],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6, 7],
    [1,2,3,4,5,6,7,8,9,10],
    [1,2,3,4,5,6,7,8,9,10,11]
]

my_list = test_cases[1]


length_list = len(my_list)

if length_list < 5:
    print("Your list is less than five.")
elif length_list >= 5 and length_list <= 10:
    print("Your list is between 5 and 10.")
else:
    print("Your list has greater than 10 values.")