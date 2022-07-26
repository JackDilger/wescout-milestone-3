from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from wescout import app, db, mongo
from wescout.models import Region, Users


# this route displays the home page where players are shown
@app.route("/")
@app.route("/get_players")
def get_players():
    players = list(mongo.db.players.find())
    return render_template("players.html", players=players)


# this route displays the regions where all scouting regions are shown
@app.route("/regions")
def regions():

    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage regions!")
        return redirect(url_for("get_players"))

    regions = list(Region.query.order_by(Region.region_name).all())
    return render_template("regions.html", regions=regions)


# this route allows admin users to add a new region
@app.route("/add_region", methods=["GET", "POST"])
def add_region():

    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage regions!")
        return redirect(url_for("regions"))

    if request.method == "POST":
        existing_region = Region.query.filter(
            Region.region_name ==
            request.form.get("region_name")).all()
        if existing_region:
            flash("Region already exists")
            return redirect(url_for("regions"))
        region = Region(region_name=request.form.get("region_name"))
        db.session.add(region)
        db.session.commit()
        flash("Region Successfully Added")
        return redirect(url_for("regions"))
    return render_template("add_region.html")


# this route allows admin user to edit a region
@app.route("/edit_region/<int:region_id>", methods=["GET", "POST"])
def edit_region(region_id):

    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage regions!")
        return redirect(url_for("regions"))

    region = Region.query.get_or_404(region_id)
    if request.method == "POST":
        existing_region = Region.query.filter(
            Region.region_name ==
            request.form.get("region_name")).all()
        if existing_region:
            flash("Region already exists")
            return redirect(url_for("regions"))
        region.region_name = request.form.get("region_name")
        db.session.commit()
        flash("Region Successfully Updated")
        return redirect(url_for("regions"))
    return render_template("edit_region.html", region=region)


# this route allows admin user to delete a new region
@app.route("/delete_region/<int:region_id>")
def delete_region(region_id):
    if "user" not in session or session["user"] != "admin":
        flash("You must be admin to manage regions!")
        return redirect(url_for("regions"))

    region = Region.query.get_or_404(region_id)
    db.session.delete(region)
    db.session.commit()
    mongo.db.players.delete_many({"region_id": str(region_id)})
    flash("Region Successfully Deleted")
    return redirect(url_for("regions"))


# this route allows users to add a new player
@app.route("/add_player", methods=["GET", "POST"])
def add_player():

    if "user" not in session:
        flash("Please log in or register to add players")
        return redirect(url_for("login"))

    if request.method == "POST":
        player = {
            "region_id": request.form.get("region_id"),
            "player_name": request.form.get("player_name"),
            "player_age": request.form.get("player_age"),
            "preferred_foot": request.form.get("preferred_foot"),
            "national_team": request.form.get("national_team"),
            "domestic_club": request.form.get("domestic_club"),
            "player_rating": request.form.get("player_rating"),
            "market_value": request.form.get("market_value"),
            "player_notes": request.form.get("player_notes"),
            "created_by": session["user"]
        }
        mongo.db.players.insert_one(player)
        flash("Player Successfully Added")
        return redirect(url_for("get_players"))

    regions = list(Region.query.order_by(Region.region_name).all())
    return render_template("add_player.html", regions=regions)


# this route allows users to edit their player information
@app.route("/edit_player/<player_id>", methods=["GET", "POST"])
def edit_player(player_id):

    player = mongo.db.players.find_one({"_id": ObjectId(player_id)})

    if "user" not in session or session["user"] != player["created_by"]:
        flash("You can only edit players you added!")
        return redirect(url_for("get_players"))

    if request.method == "POST":
        submit = {
            "region_id": request.form.get("region_id"),
            "player_name": request.form.get("player_name"),
            "player_age": request.form.get("player_age"),
            "preferred_foot": request.form.get("preferred_foot"),
            "national_team": request.form.get("national_team"),
            "domestic_club": request.form.get("domestic_club"),
            "player_rating": request.form.get("player_rating"),
            "market_value": request.form.get("market_value"),
            "player_notes": request.form.get("player_notes"),
            "created_by": session["user"]
        }
        mongo.db.players.replace_one({"_id": ObjectId(player_id)}, submit)
        flash("Player Successfully Updated")
        return redirect(url_for("get_players"))

    regions = list(Region.query.order_by(Region.region_name).all())
    return render_template("edit_player.html", player=player, regions=regions)


# this route allows users to delete their player information
@app.route("/delete_player/<player_id>")
def delete_player(player_id):

    player = mongo.db.players.find_one({"_id": ObjectId(player_id)})

    if "user" not in session or session["user"] != player["created_by"]:
        flash("You can only delete players you added!")
        return redirect(url_for("get_players"))

    mongo.db.players.delete_one({"_id": ObjectId(player_id)})
    flash("PLayer Successfully Deleted")
    return redirect(url_for("get_players"))


# this route allows users to register
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        existing_user = Users.query.filter(
            Users.user_name ==
            request.form.get("username").lower()).all()
        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))
        user = Users(
            user_name=request.form.get("username").lower(),
            password=generate_password_hash(request.form.get("password"))
        )
        db.session.add(user)
        db.session.commit()

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# this route renders the user profile
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):

    if "user" not in session:
        flash("Please log in or register to access your profile")
        return redirect(url_for("login"))

    if "user" in session:
        return render_template("profile.html", username=session["user"])

    return redirect(url_for("register"))


# this route allows users to login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":

        existing_user = Users.query.filter(
            Users.user_name ==
            request.form.get("username").lower()).all()

        if existing_user:
            print(request.form.get("username"))
            if check_password_hash(
                    existing_user[0].password, request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:

            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# this route allows users to logout
@app.route("/logout")
def logout():

    if "user" not in session:
        flash("You're not logged in!")
        return redirect(url_for("login"))

    flash("Successfully logged out")
    session.pop("user")
    return redirect(url_for("login"))


# this route esnures only registered users can add players
@app.route("/add_player_btn")
def add_player_btn():

    if "user" not in session:
        flash("You must regsiter to add players!")
        return redirect(url_for("register"))

    return render_template("add_player.html")


# this route allows users to use the text index search
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    players = list(mongo.db.players.find({"$text": {"$search": query}}))
    return render_template("players.html", players=players)


# this route handles 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# this route handles 500 errors
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500
