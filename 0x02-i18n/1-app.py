import uuid

from flask import Flask, g, render_template, request, flash
import uuid
from flask_babel import Babel, _


def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app = Flask(__name__)
babel = Babel(app, locale_selector=get_locale)


class Config:
    BABEL_LOCALE = "fr"
    BABEL_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]

    SECRET_KEY = uuid.uuid4().hex


# Configurations of the app
app.config.from_object(Config)


@app.route("/")
def index():
    flash(_('Your post is now live!'))
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
