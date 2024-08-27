#!/usr/bin/env python3
"""app server for flask"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """config class for Babel"""
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get user best language match"""
    return request.accept_languages.best_match(['en', 'fr'])


@app.route('/')
def index():
    """main default route"""
    title = "Welcome to Holberton"
    body = "Hello world"
    return render_template('0-index.html', title=title, body=body)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
