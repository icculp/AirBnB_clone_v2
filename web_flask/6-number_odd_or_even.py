#!/usr/bin/python3
'''
    Task 6
'''
from flask import Flask
from flask import render_template


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


@app.route('/number/<text>', strict_slashes=False)
def hello_number(text):
    ''' Hello HBNB! '''
    if type(eval(text)) is int:
        return "{} is a number".format(text)


@app.route('/number_template/<n>', strict_slashes=False)
def hello_number_template(n):
    ''' Hello HBNB! '''
    if type(eval(n)) is int:
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def hello_number_odd_or_even(n):
    ''' Hello HBNB! '''
    if type(eval(n)) is int:
        return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)