#!/usr/bin/python3
'''
    Task 0
'''
from flask import Flask
from web_flask import app


@app.route('/', strict_slashes=False)
def hello_hbnb():
    ''' Hello HBNB! '''
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(debug=True)