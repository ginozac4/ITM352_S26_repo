# Name: Cassiddy Ginoza
# Date: Jan. 29, 2026

responseValues = [5, 7, 3, 8]
responseValues.append(0)
print("After appending 0:", responseValues)

#responseValues.insert(2,6)
responseValues = responseValues[:2] + [6] + responseValues[2:] 
    # take the list up to index 2, add 6, then add the rest of the list
print("After inserting 6 at index 2:", responseValues)


