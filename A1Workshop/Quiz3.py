#Quiz game. Third version
#Name: Cassiddy Ginoza
#Date: Feb. 24, 2026
# Make QUESTIONS a dictionary, to include answer options and the correct choice.

QUESTIONS = {
    "What is the airspeed of an unladen swallow in miles/hr? ": ("12", "10", "15", "0"),
    "What is the capital of Texas? ": ("Austin", "Houston", "Dallas", "San Antonio"),
    "The Last Supper was painted by which artist? ": ("Da Vinci", "Michelangelo", "Raphael", "Donatello")
    }

for question, options in QUESTIONS.items():
    correct_answer = options[0] 
    for alternative in sorted(options):
        print(f" - {alternative}")

    answer = input(question + ": ")
    if answer == correct_answer:
        print("Correct!")
    else:       
        print(f"The answer is {correct_answer!r}, not {answer!r}.")

