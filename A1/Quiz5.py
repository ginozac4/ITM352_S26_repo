#Quiz game. Fifth version
#Name: Cassiddy Ginoza
#Date: Feb. 24, 2026
# Improve look and usability, keep track of correct answers.

from string import ascii_lowercase
QUESTIONS = { 
    "What is the airspeed of an unladen swallow in miles/hr? ": ("12", "10", "15", "0"),
    "What is the capital of Texas? ": ("Austin", "Houston", "Dallas", "San Antonio"),
    "The Last Supper was painted by which artist? ": ("Da Vinci", "Michelangelo", "Raphael", "Donatello")
    }

num_correct = 0
for num, (question, options) in enumerate(QUESTIONS.items(), start=1):
    print(f"Question {num}:")
    print(question)
    correct_answer = options[0]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(options)))
    for label, alternative in labeled_alternatives.items():
        print(f" {label}. {alternative}")

    answer_label = input("Choice? ")
    answer = labeled_alternatives.get(answer_label)
    if answer == correct_answer:
        print("Correct!")
        num_correct += 1
    else:       
        print(f"The answer is {correct_answer!r}, not {answer!r}.")

print(f"You got {num_correct} out of {len(QUESTIONS)} correct.")