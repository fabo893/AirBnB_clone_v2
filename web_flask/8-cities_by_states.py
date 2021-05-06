#!/usr/bin/python3
"""
    Hello Flask!
"""


from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception=None):
    """ Call method close """
    storage.close()


@app.route('/cities_by_states')
def states_list():
    """ Render Template """
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
    app.run(debug=True)