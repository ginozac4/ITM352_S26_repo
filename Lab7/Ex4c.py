#create a function that will print if the purchase is within the budget or not
# Name: Cassiddy Ginoza
# Date: Feb. 19, 2026

def check_budget(recent_purchases, budget):
    results = [] 

    for purchase in recent_purchases:
        if purchase > budget:
            results.append(f"This purchase is over budget: {purchase}")
        else:
            results.append(f"This purchase is within budget: {purchase}")
    
    return results

#recent_purchase = [500.70, 450.23, 200.58, 450.38, 92.34]
#budget = 500

#recent_purchase = [3.40, 2.68, 67.23, 24.53, 23.94]
#budget = 24

recent_purchase = [100.00, 150.00, 200.00, 250.00, 300.00]
budget = 200

print(check_budget(recent_purchase, budget))