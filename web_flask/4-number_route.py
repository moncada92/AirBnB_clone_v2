#!usr/bin/env python3
"""
create second route with variables
"""

from flask import Flask, escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def start_app():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB!'


@app.route('/c/<var>')
def path(var):
    return 'C %s' % escape(var.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyis(text="is cool"):
    return 'Python %s' % escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_num(n):
    return '%d is a number' % n


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")