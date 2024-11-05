"""
This module import a simple flask app
"""

from flask import Flask, g, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """This is the config
    class used to configure our app
    """
    BABEL_LOCALE = "fr"
    BABEL_TIMEZONE = "UTC"
    LANGUAGES = ["en", "fr"]


# Configurations of the app
app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def index():
    """THis is a simple index page rendered
    by this view
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
