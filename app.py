from flask import Flask, jsonify, g
from flask_cors import CORS

from resources.expenses import expense
from resources.categories import category

import models

DEBUG = True
PORT = 8000

# Initialize an instance of the Flask class.
# This starts the website!
app = Flask(__name__)

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()


@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response


CORS(expense, origins=['http://localhost:3000'], supports_credentials=True) 
CORS(category, origins=['http://localhost:3000'], supports_credentials=True) 


app.register_blueprint(expense, url_prefix='/api/v1/expenses') 
app.register_blueprint(category, url_prefix='/api/v1/categories') 

# The default URL ends in / ("my-website.com/").
@app.route('/')
def index():
    return 'Flask app is up on port #8000'

# Run the app when the program starts!
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)