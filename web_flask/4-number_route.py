#!/usr/bin/python3
""" Script that starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnh():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    text = text.replace('_', ' ')
    return 'C %s' % text


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text):
    text = text.replace('_', ' ')
    return 'Python %s' % text


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return '%s is a number' % n


if __name__ == "__main__":
    app.run(debug=True)
