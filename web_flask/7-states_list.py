#!/usr/bin/python3
"""
Flask Web Application for Displaying States

This script initializes a Flask web application that retrieves and displays a 
list of states from a database in alphabetical order. The application uses a 
templating engine to render the states on an HTML page.

Modules:
    - Flask: A lightweight WSGI web framework for Python.
    - render_template: Function to render HTML templates with dynamic content.
    - models: Imports all models from the project.
    - storage: Handles database interactions using an ORM.

Routes:
    - /states_list: Displays a list of states ordered alphabetically.
    
Teardown:
    - Closes the database session after each request.

Author: Your Name
Date: YYYY-MM-DD
"""

from flask import Flask, render_template
from models import *
from models import storage

# Initialize Flask application
app = Flask(__name__)

@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Handles the /states_list route.

    Retrieves all State objects from the database, sorts them alphabetically 
    by name, and passes them to an HTML template for rendering.

    Returns:
        str: Rendered HTML page displaying a list of states.
    """
    # Fetch all states and sort them by name
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    
    # Render the states list using the template
    return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the database connection after each request.

    This function ensures that the storage session is properly closed to 
    prevent memory leaks and maintain database efficiency.

    Args:
        exception (Exception): Exception raised during the request, if any.
    """
    storage.close()

# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
