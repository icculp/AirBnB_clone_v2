#!/usr/bin/python3
'''
    Task 4
'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hello_hbnb():
    ''' Hello HBNB! '''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    ''' Hello HBNB! '''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    ''' Hello HBNB! '''
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text=None):
    ''' Hello HBNB! '''
    if text is not None:
        return "Python {}".format(text.replace("_", " "))
    else:
        return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    ''' Hello HBNB! '''
    if n.isdigit():
        return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
