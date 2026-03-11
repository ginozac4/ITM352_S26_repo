# Program to remove any scores from a list that are below 50.
 
scores = [60, 45, 30, 85, 10, 90] 
scores_new = []

for score in scores: 
    if score >= 50: 
        scores_new.append(score) 
print(scores_new) 
