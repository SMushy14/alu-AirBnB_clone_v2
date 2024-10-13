#!/usr/bin/python3
"""
Start a web application with two routing endpoints.

This module initializes a Flask web application and defines a route
to render a list of states stored in the database. It utilizes the
Flask framework to handle web requests and responses.
"""

from models import storage
from models.state import State
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

@app.route('/states_list')
def states_list():
    """
    Render a template displaying a list of states.

    This route retrieves all State objects from storage, sorts them 
    alphabetically by name, and renders the '7-states_list.html' 
    template with the sorted states.

    Returns:
        str: Rendered HTML template displaying the sorted list of states.
    """
    path = '7-states_list.html'  # Path to the HTML template
    states = storage.all(State)  # Retrieve all State objects from storage
    # Sort State objects alphabetically by name
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template(path, sorted_states=sorted_states)


@app.teardown_appcontext
def app_teardown(arg=None):
    """
    Clean up the application context.

    This function is called at the end of each request, ensuring that
    the storage session is properly closed to free up resources.

    Args:
        arg (optional): An optional argument that can be passed.
    """
    storage.close()  # Close the storage session


if __name__ == '__main__':
    # Set the Flask application to allow URLs without strict trailing slashes
    app.url_map.strict_slashes = False
    # Run the Flask application, listening on all interfaces at port 5000
    app.run(host='0.0.0.0', port=5000)
