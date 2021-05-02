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


if __name__ == "__main__":
    app.run(debug=True)
