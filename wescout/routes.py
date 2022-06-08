from flask import render_template
from wescout import app, db
from wescout.models import Region, Users


@app.route("/")
def home():
    return render_template("players.html")