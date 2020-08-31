#!/usr/bin/python3
'''
    Task 0
'''
from flask import Flask
from web_flask import app


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
