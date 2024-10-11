#!/usr/bin/python3

"""A script that starts a Flask web application
listening on 0.0.0.0, port 5000 at the /route display
Hello HBNB!, at /hbnb route display HBNB and at
/c/<text> display C followed by the value of the
text variable, replace underscore _ symbols with a space"""

from flask import Flask

my_app = Flask(__name__)


@my_app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@my_app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@my_app.route('/c/<text>', strict_slashes=False)
def text_display(text):
    return "C {}".format(text.replace('_', ' '))

if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=5000)
