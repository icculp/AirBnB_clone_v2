#!/usr/bin/python3
'''
    Task 10
'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity


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
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_number_template(n):
    ''' Hello HBNB! '''
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hello_number_odd_or_even(n):
    ''' Hello HBNB! '''
    return render_template("6-number_odd_or_even.html", n=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    ''' Hello HBNB! '''
    sto = storage.all(State).values()
    return render_template("7-states_list.html", sto=sto)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    ''' Hello HBNB! '''
    sto = storage.all(State).values()
    return render_template("8-cities_by_states.html", sto=sto)


@app.route('/states', strict_slashes=False)
def states():
    ''' Hello HBNB! '''
    sto = storage.all(State)
    id = None
    return render_template("9-states.html", sto=sto, id=id)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    ''' Hello HBNB! '''
    sto = storage.all(State)
    id = 'State.' + str(id)
    return render_template("9-states.html", sto=sto, id=id)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    ''' Hello HBNB! '''
    sto = storage.all(State)
    am = storage.all(Amenity)
    '''
    print(dir(am))
    for i in am.values():
        print(i)
        break
    '''
    return render_template("10-hbnb_filters.html", sto=sto, am=am)

@app.teardown_appcontext
def close_db(self):
    """ Closes the connection at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
