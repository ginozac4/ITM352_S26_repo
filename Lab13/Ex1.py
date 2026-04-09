# Name: Cassiddy Ginoza
# Date: Apr. 9, 2026

# create a simple HTML Flask application that displays a welcome message

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) # create an application
# route = path user specifies after server name

@app.route('/')
def index(): #function that gets called when path matched
    return ("Welcome to Ginoza's really boring web page")

if __name__ == '__main__':
    app.run(debug=True) # run in debug mode