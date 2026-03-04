from string import ascii_lowercase
import A1_QuizQuestions
QUESTIONS = A1_QuizQuestions.QUESTIONS

def quiz():
    num_correct = 0
    for question_number, (question, (choices, explanation)) in enumerate(QUESTIONS.items(), start=1):
        # starts at 1, and unpacks the question, options, and explanation from the QUESTIONS dictionary
        print(f"Question {question_number}:")
        print(question)
        
        correct_answer = choices[0]
        #the correct answer is always the first option in the list

        answer_choices = dict(zip(ascii_lowercase, sorted(choices)))
        # creates a dictionary, assigning letters a, b, c, and d to the options
        for letter, assigned_answer in answer_choices.items():
            print(f" {letter}. {assigned_answer}")
        
        # Prompt user input until valid
        while True:
            answer_label = input("Choice? ")
            if answer_label in answer_choices:
                break
            print("Invalid choice - please enter one of:", ", ".join(answer_choices.keys()))
        # checks to see if the user input is valid, and breaks the while loop that re-prompts
        # the user if user enters a valid choice.
        
        answer = answer_choices.get(answer_label)
        # gets the answer corresponding to the user's choice from the answer_choices dictionary
        
        if answer == correct_answer:
            print("Correct!")
            print(explanation)
            # prints the explanation when user gets the answer correct
            num_correct += 1
        else:
            print(f"The answer is {correct_answer}, not {answer}.")

    print(f"You got {num_correct} out of {len(QUESTIONS)} correct.")
    
    with open("quiz_history.txt", "a") as history_file:
        # opens the quiz_history.txt file so it can be appended to
        history_file.write(f"Score: {num_correct} out of {len(QUESTIONS)}\n")
        # tells the code what to write to the file and adds a new line after each score
    
    play_again = input("Would you like to play again? (Y/N) ")
    if play_again == "Y":
        quiz()
    else:
        print("Thanks for playing!")

quiz()