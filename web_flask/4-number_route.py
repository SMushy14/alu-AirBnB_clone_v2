#!/usr/bin/python3

"""A script that starts a Flask web application
listening on 0.0.0.0, port 5000 at the /route display
Hello HBNB!, at /hbnb route display HBNB /c/<text>
display C followed by the value of the text variable,
replace underscore _ symbols with a space, at
/python/(<text>) display Python followed by the value
of the text variable (replace underscore _ symbols with a space
while default value of text is ~is cool and at /number/<n>
display n is a number only if n is an integer"""

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


@my_app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@my_app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python {}".format(text.replace('_', ' '))


@my_app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)

if __name__ == "__main__":
    my_app.run(host="0.0.0.0", port=5000)
