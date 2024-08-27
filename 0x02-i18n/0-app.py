#!/usr/bin/env python3
"""app server for flask"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """main default route"""
    title = "Welcome to Holberton"
    body = "Hello world"
    return render_template('0-index.html', title=title, body=body)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
