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


@app.route("/regions")
def regions():
    regions = list(Region.query.order_by(Region.region_name).all())
    return render_template("regions.html", regions=regions)


@app.route("/add_region", methods=["GET", "POST"])
def add_region():
    if request.method == "POST":
        region = Region(region_name=request.form.get("region_name"))
        db.session.add(region)
        db.session.commit()
        return redirect(url_for("regions"))
    return render_template("add_region.html")


@app.route("/edit_region/<int:region_id>", methods=["GET", "POST"])
def edit_region(region_id):
    region = Region.query.get_or_404(region_id)
    if request.method == "POST":
        region.region_name = request.form.get("region_name")
        db.session.commit()
        return redirect(url_for("regions"))
    return render_template("edit_region.html", region=region)


@app.route("/delete_region/<int:region_id>")
def delete_region(region_id):
    region = Region.query.get_or_404(region_id)
    db.session.delete(region)
    db.session.commit()
    mongo.db.players.delete_many({"region_id": str(region_id)})
    return redirect(url_for("regions"))


@app.route("/add_player")
def add_player():
    return render_template("add_player.html")






