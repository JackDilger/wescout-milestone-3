from wescout import db


class Region(db.Model):
    # schema for the Region model
    id = db.Column(db.Integer, primary_key=True)
    region_name = db.Column(db.String(25), unique=True, nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.region_name


class Users(db.Model):
    # schema for the Users model
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(260), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.user_name