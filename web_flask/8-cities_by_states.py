#!/usr/bin/python3
"""
Write a script that starts a Flask web application:
-After each request you must remove the current SQLAlchemy Session:
Declare a method to handle @app.teardown_appcontext
Call in this method storage.close()
-Routes:
/cities_by_states: display a HTML page: (inside the tag BODY)
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


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """ Displays a specific message when route is '/cities_by_states' """
    return render_template('8-cities_by_states.html',
                           states=storage.all("State").values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
