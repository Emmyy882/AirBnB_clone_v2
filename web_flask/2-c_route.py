#!/usr/bin/python3
"""A Script that starts a flask web application"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """Home Page"""
    return f'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """HBNB Page"""
    return f'HBNB'


@app.route('/c/<text>')
def text(text):
    """text page - displays 'C' followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
