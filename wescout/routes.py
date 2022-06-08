from flask import flash, render_template, request, redirect, session, url_for
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from wescout import app, db, mongo
from wescout.models import Region, Users


@app.route("/")
def home():
    return render_template("players.html")

