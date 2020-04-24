#I'm just going to make my own Flask webpage and have users go to mine.

from flask import Flask

app = Flask(__name__)

@app.route('/')

@app.route('/UserPage')
def hello_world():
    return "<><>"