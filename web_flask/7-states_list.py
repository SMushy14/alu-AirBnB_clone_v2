#!/usr/bin/python3
"""Module that starts a Flask web application.

This module sets up a simple Flask web application that provides a route
to display a list of states stored in a database. The states are fetched
from the storage, sorted alphabetically, and rendered in an HTML template.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Returns an HTML page with a list of all States in the database.

    This route handles GET requests to '/states_list'. It retrieves all
    states from the database, sorts them by name, and renders them using
    the '7-states_list.html' template.

    Returns:
        str: Rendered HTML template containing the list of states.
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def close_session(exception):
    """Closes the session after each request.

    This function is called after each request, ensuring that any
    resources allocated during the request (e.g., database sessions)
    are properly closed.

    Args:
        exception: The exception raised during the request, if any.
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
