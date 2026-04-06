#Quiz game. Fourth version
#Name: Cassiddy Ginoza
#Date: Feb. 24, 2026
#Make questions a dictionary, to include answer options and the correct choice.
# allow the user to select the correct answer by a label.

QUESTIONS = { 
    "What is the airspeed of an unladen swallow in miles/hr? ": ("12", "10", "15", "0"),
    "What is the capital of Texas? ": ("Austin", "Houston", "Dallas", "San Antonio"),
    "The Last Supper was painted by which artist? ": ("Da Vinci", "Michelangelo", "Raphael", "Donatello")
    }

for question, options in QUESTIONS.items():
    correct_answer = options[0] 
    sorted_options = sorted(options)
    for label, alternative in enumerate(sorted_options, start=1):
        print(f" {label}. {alternative}")

    answer_label = int(input(question + ": "))
    answer = sorted_options(answer_label - 1)
    if answer == correct_answer:
        print("Correct!")
    else:       
        print(f"The answer is {correct_answer!r}, not {answer!r}.")
