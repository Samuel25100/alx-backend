#!/usr/bin/env python3
"""app server for flask"""
from flask import Flask, render_template, request, g
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
    elif g.user is not None and g.user["locale"] in Config.LANGUAGES:
        return g.user["locale"]
    elif request.accept_languages.best_match(Config.LANGUAGES):
        return request.accept_languages.best_match(Config.LANGUAGES)
    else:
        return Config.BABEL_DEFAULT_LOCALE


def get_user(id):
    """mock the login system based on user data"""
    users = {
            1: {"name": "Balou", "locale":
                "fr", "timezone": "Europe/Paris"},
            2: {"name": "Beyonce", "locale":
                "en", "timezone": "US/Central"},
            3: {"name": "Spock", "locale":
                "kg", "timezone": "Vulcan"},
            4: {"name": "Teletubby", "locale": None,
                "timezone": "Europe/London"},
    }
    if id in users:
        return users[id]
    return None


@app.before_request
def before_request():
    """run before before any request"""
    user_id = request.args.get('login_as')
    if user_id:
        g.user = get_user(int(user_id))
    else:
        g.user = None


@app.route('/')
def index():
    """main default route"""
    if g.user is not None:
        username = g.user["name"]
        return render_template('5-index.html', username=username)
    else:
        return render_template('5-index.html', username=None)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
