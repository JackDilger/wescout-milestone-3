from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from wescout import app, db, mongo
from wescout.models import Region, Users


@app.route("/")
@app.route("/get_players")
def get_players():
    players = list(mongo.db.players.find())
    return render_template("players.html", players=players)


@app.route("/region")
def region():
    return render_template("region.html")


@app.route("/add_region", methods=["GET", "POST"])
def add_region():
    if request.method == "POST":
        region = Region(region_name=request.form.get("region_name"))
        db.session.add(region)
        db.session.commit()
        return redirect(url_for("region"))
    return render_template("add_region.html")


