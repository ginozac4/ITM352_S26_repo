from flask import Flask, render_template, request, redirect, url_for, session
    # session is used to temporarily keep track of a user's progress 
import json
import random
    # random is used to shuffle the questions.

app = Flask(__name__)
app.secret_key = "secret" 

with open("south_park_questions.json", "r") as f:
    questions = json.load(f)
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if "index" not in session: 
        # this code initializes a session for the user if it's their first time accessing.
        session["index"] = 0
        # index is the question number.
        session["score"] = 0
        # score is the correct answers user answers.
        session["question_order"] = list(range(len(questions)))
        random.shuffle(session["question_order"])
        # this code was created by AI, using the prompt "How would I use random in order to shuffle the questions for the user?"


    if session["index"] >= len(questions):
        return redirect(url_for("result"))
        # this code will end and redirect to result if index is equal to length of questions

    if request.method == "POST": # user submits an answer from the page
        user_answer = request.form.get("answer") # compares user's answer to correct answer from the list.
        if user_answer:
            q_index = session["question_order"][session["index"]]
            current_q = questions[q_index]  
            # if the user submits an answer, it will retrieve the question from the 
            # questions list by its index.
            if user_answer == current_q["answer"]:
                session["score"] += 1
                # if the answer matches the current question, the session adds 1 to the score.
            session["explanation"] = current_q["explanation"]
            # this code provides an explanation for the answer despite whether the answer is correct.
        session["index"] += 1
        # the index moves on to the next question.
        session.pop("choices", None) 
        # this code removes the choices from the session so that a new set of choices can be shuffled for the next question,
        # since it created a new list of choices.

        if session["index"] >= len(questions):
            return redirect(url_for("result"))
        # this code moves to the result page if the index is equal to the length of questions list.
        
    q_index = session["question_order"][session["index"]]
    q = questions[q_index]

    if "choices" not in session:
        choices = q["choices"][:]
        # this code creates a copy of the choices list.
        random.shuffle(choices)
        # this code shuffles the choices.
        session["choices"] = choices
    # this code was created by AI, using the prompt "How would I use random to shuffle the choices for each question?"

    return render_template("quiz.html", question=q, choices=session["choices"])

@app.route("/result")
def result():
    # Get score from session and render result page
    score = session.get("score", 0)
    session.clear()  # Clear session after showing result
    return render_template("result.html", score=score, total=len(questions))

def main():
    app.run(debug=True)

if __name__ == "__main__":
    main()