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


@app.route("/add_player", methods=["GET", "POST"])
def add_player():
    if request.method == "POST":
        player = {
            "region_id": request.form.get("region_id"),
            "player_name": request.form.get("player_name"),
            "player_age": request.form.get("player_age"),
            "preferred_foot": request.form.get("preferred_foot"),
            "national_team": request.form.get("national_team"),
            "domestic_club": request.form.get("domestic_club"),
            "player_rating": request.form.get("market_value"),
            "market_value": request.form.get("market_value"),
            "player_notes": request.form.get("player_notes") 
        }
        mongo.db.players.insert_one(player)
        flash("Player Successfully Added")
        return redirect(url_for("get_players"))

    regions = list(Region.query.order_by(Region.region_name).all())
    return render_template("add_player.html", regions=regions)


@app.route("/edit_player/<player_id>", methods=["GET", "POST"])
def edit_player(player_id):

    player = mongo.db.players.find_one({"_id": ObjectId(player_id)})

    regions = list(Region.query.order_by(Region.region_name).all())
    return render_template("edit_player.html", player=player, regions=regions)



