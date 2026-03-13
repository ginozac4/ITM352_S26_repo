# Open a text file and print its type
#file_object = open("names.txt")'''
with open("names.txt") as file_object:
    print(type(file_object))
    #file_object.close()