shopping_list = []

shopping_list.append("Apples")
shopping_list.append("Bananas")
shopping_list.append("Carrots")
shopping_list.insert(0, "Eggs")
shopping_list.append("Eggs")
shopping_list.remove("Apples")
shopping_list.pop() # removes the last item
shopping_list.sort()
# index refers to position in the list, starting from 0

print("Current shopping list:", shopping_list)