"""
This module import a simple flask app
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """This method open a simple html template"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
