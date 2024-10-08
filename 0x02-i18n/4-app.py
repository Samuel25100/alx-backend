#!/usr/bin/env python3
"""app server for flask"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


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
    loc = request.args.get('locale')
    if loc in Config.LANGUAGES:
        return loc
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """main default route"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
