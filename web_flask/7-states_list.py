#!/usr/bin/python3
"""A script that starts a Flask web application.

This web application listens on 0.0.0.0 at port 5000. It fetches data
from the storage engine (FileStorage or DBStorage) and displays a list
of all State objects present in the database.

Routes:
    - /states_list: Displays an HTML page with a list of states sorted
      by name (A to Z). Each state is shown in a list item with its
      ID and name.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays a list of all State objects in the database.

    Retrieves all states from the storage, sorts them by name, and
    renders them in an HTML template.

    Returns:
        str: Rendered HTML template containing the list of states.
    """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def close_session(exception):
    """Closes the current SQLAlchemy session after each request.

    This function is called automatically at the end of each request
    to clean up the resources and close the session.

    Args:
        exception: Any exception raised during the request.
    """
    storage.close()

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=True)
