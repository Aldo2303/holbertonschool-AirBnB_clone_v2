#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
-After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
"""
from flask import Flask
from flask import render_template
from models import storage
from models import *
app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(exception):
    """Call in this method storage.close()"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Displays a specific message when route is '/states_list' """
    return render_template('7-states_list.html',
                           states=storage.all("State").values())


@app.route('/states/<id>')
def if_stateID(id):
    """Displays a specific message when route is '/states/<id>'"""
    state_obj = None
    for state in storage.all("State").values():
        if state.id == id:
            state_obj = state
    return render_template('9-states.html',
                           state_obj=state_obj)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
