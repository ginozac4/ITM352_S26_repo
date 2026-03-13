#use readlines() to print the contents of the file as a list.

with open("names.txt") as file_object:
    contents_list = file_object.readlines()
    print(contents_list)