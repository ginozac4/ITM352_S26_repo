#create a function that will print if the purchase is within the budget or not

def check_budget(recent_purchases, budget):
    total_spent = 0
    results = [] 

    for purchase in recent_purchases:
        total_spent += purchase
        if total_spent > budget:
            results.append(f"This purchase is over budget: {purchase}")
        else:
            results.append(f"This purchase is within budget: {purchase}")
    
    return results

recent_purchase = [36.13, 23.87, 103.35, 22.93, 11.62]
budget = 50

check_budget(recent_purchase, budget)