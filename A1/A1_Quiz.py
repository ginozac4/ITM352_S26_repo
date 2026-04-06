from string import ascii_lowercase
import A1.A1_SouthParkQuestions as A1_SouthParkQuestions
import A1.A1_FootballMascotQuestions as A1_FootballMascotQuestions

def user_quiz_selection():
    print("Which quiz would you like to play?")
    print("1. South Park Questions")
    print("2. Football Mascot Questions")
    # prints the quiz name options for the user to choose from
    
    while True:
        choice = input("Enter your choice (1 or 2): ")
        if choice == "1":
            return A1_SouthParkQuestions.QUESTIONS
        elif choice == "2":
            return A1_FootballMascotQuestions.QUESTIONS
        else:
            print("Invalid choice - please enter 1 or 2.")
    # loop that prompts the user to enter a valid choice, and will loop a re-prompt until they do

def quiz():
    QUESTIONS = user_quiz_selection()
    # gets the quiz questions from the user's selection and returns the questions (from the loop in the function)
    num_correct = 0
    for question_number, (question, (choices, explanation)) in enumerate(QUESTIONS.items(), start=1):
        # starts at 1, and unpacks the question, options, and explanation from the QUESTIONS dictionary
        print(f"Question {question_number}:")
        print(question)
        
        correct_answer = choices[0]
        # the correct answer is always the first option in the list

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
            # Requirement 7: prints the explanation for why the correct answer is the correct answer
            num_correct += 1
        else:
            print(f"The answer is {correct_answer}, not {answer}.")

    print(f"You got {num_correct} out of {len(QUESTIONS)} correct.")
    
    # Requirement 1:
    with open("quiz_history.txt", "a") as history_file:
        # opens the quiz_history.txt file so it can be appended to
        #add the quiz name to the file
        if QUESTIONS == A1_SouthParkQuestions.QUESTIONS:
            history_file.write(f"South Park Quiz: {num_correct} out of {len(QUESTIONS)}\n")
        elif QUESTIONS == A1_FootballMascotQuestions.QUESTIONS:
            history_file.write(f'Football Mascot Quiz: {num_correct} out of {len(QUESTIONS)}\n')
            # \n prints new line after each quiz result is added to the file
    
    play_again = input("Would you like to play again? (Y/N) ")
    if play_again == "Y" or play_again == "y":
        quiz()
    else:
        print("Thanks for playing!")

quiz()