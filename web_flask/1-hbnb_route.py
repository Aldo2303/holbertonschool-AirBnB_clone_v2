#!/usr/bin/python3
"""
Script that starts a Flask web application:
- Must be listening on 0.0.0.0, port 5000
- Routes:
    '/': display “Hello HBNB!”
    '/hbnb': display "HBNB"
- Option strict_slashes=False in route definition
"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Displays a specific message when route is '/' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays a specific message when route is '/hbnb' """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
