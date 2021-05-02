#!/usr/bin/python3
""" Script that starts a Flask web application """
from models.state import State
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    states = storage.all(State)
    if id:
        id = "State." + id
        if id in states:
            states = states[id]
        else:
            states = None
    else:
        states = states.values()
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == "__main__":
    app.run(debug=True)
