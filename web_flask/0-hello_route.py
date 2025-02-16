#!/usr/bin/python3
"""A Script that starts a flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """displays 'Hello HBNB!' when route is accessed"""
    return f'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
