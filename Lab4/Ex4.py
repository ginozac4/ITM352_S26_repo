# Name: Cassiddy Ginoza
# Date: Jan. 29, 2026

survey_responses = (1012, 1035, 1021, 1053)
print("Original survey responses tuple:", survey_responses)
# survey_responses.append(1011) # This will raise an AttributeError
survey_responses = survey_responses + (1011,)
print("After adding 1011: ", survey_responses)