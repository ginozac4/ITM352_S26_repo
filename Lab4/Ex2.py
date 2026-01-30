#Define a list of survey response variables and store them in variable, then define 
# tuple of respondent ID values. Use the .append() method to append the tuple to the 
# list, then print out the list.
# Name: Cassiddy Ginoza
# Date: Jan. 29, 2026

'''responses = [5, 7, 3, 8]
respondent_ids = (1012, 1035, 1021, 1053)
responses.append(respondent_ids)
print("Survey responses with respondent IDs:", responses)'''

response_values = [(1012, 5), (1035, 7), (1021, 3), (1053, 8)]
response_values.sort()
print("Sorted survey responses with respondent IDs:", response_values)