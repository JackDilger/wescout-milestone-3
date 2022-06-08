from flask import render_template
from wescout import app, db


@app.route("/")
def home():
    return render_template("base.html")