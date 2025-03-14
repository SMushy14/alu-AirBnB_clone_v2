#!/usr/bin/python3

"""A script that starts a Flask web application
listening on 0.0.0.0, port 5000
and also at the /hbnb route. display Hello HBNB! """

from flask import Flask

my_app = Flask(__name__)


@my_app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@my_app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=5000)
