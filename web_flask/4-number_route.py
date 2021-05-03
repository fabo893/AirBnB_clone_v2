#!/usr/bin/python3
"""
    Hello Flask!
"""


from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Hello method """
    return "Hello HBNB!"


@app.route('/hbnb')
def hello123():
    """ Second hello method """
    return "HBNB"


@app.route('/c/<text>')
def cprint(text):
    """ Display C with text """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def pythonprint(text):
    """ Display Python with text """
    if len(text) > 0:
        text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def number(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(debug=True)
