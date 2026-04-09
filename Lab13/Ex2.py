# Name: Cassiddy Ginoza
# Date: Apr. 9, 2026

# if they've logged in successfully, load a success page
# will load them into a site

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userid = request.form['username']
        password = request.form['password']
        # Replace this with your actual authentication logic
        if USERS.get(userid) == password:
            return redirect(url_for('success', username=userid))
        else:
            return "Sorry. Try again."
    else:
        return render_template('login.html')

@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

USERS = {"port": "port123",
        "kazman": "kazman123"}


if __name__ == '__main__':
    app.run(debug=True)