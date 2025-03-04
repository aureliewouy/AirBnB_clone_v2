#!/usr/bin/python3
""" Script that starts a Flask web application """
from models.state import State
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
