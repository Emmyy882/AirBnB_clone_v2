#!/usr/bin/python3
"""A Script that starts a flask web application"""
from flask import Flask
from markupsafe import escape
from flask import render_template


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


# @app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_page(text='is cool'):
    """Python page: displays 'Python' followed by the value of the text"""
    for ch in text:
        if ch == '_':
            texts = text.split('_')

            new_text = ''
            for i in range(len(texts)):
                new_text += ' ' + texts[i]
            return f'Python{new_text}'
    return f'Python {text}'


@app.route('/number/<int:n>')
def number(n):
    """Number Page: display 'n is a number' only if n is an integer"""
    if isinstance(n, int):
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n=None):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n=None):
    """display a HTML page only if n is an integer, indicating if n is an
    even or odd number"""
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=None)
