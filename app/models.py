# from app import db

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    registered_on = db.Column('registered_on', db.DateTime)
    user_role = db.Column(db.String(80))
    notes = db.relationship('Note', backref='user', lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_urole(self):
        return self.user_role

class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(12))
    time = db.Column(db.String(10))
    duration = db.Column(db.String(12))
    regNum = db.Column(db.Integer)
    droneNum = db.Column(db.Integer)
    pilot = db.Column(db.String(32))
    pilotNum = db.Column(db.Integer)
    location = db.Column(db.String(50))
    altitude = db.Column(db.Integer)
    weather = db.Column(db.String(16))
    distance = db.Column(db.Integer)
    notes = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return "{{\"Date\": \"{}\", \"time\": \"{}\",\
        \"duration\": \"{}\", \"regNum\": {}, \"droneNum\": \"{}\",\
        \"pilot\": \"{}\", \"pilotNum\": {}, \"location\": \"{}\",\
        \"altitude\": {}, \"weather\": \"{}\", \"distance\": {},\
        \"notes\": \"{}\"}}".format(self.date, self.time, self.duration,
        self.regNum, self.droneNum, self.pilot, self.pilotNum,
        self.location, self.altitude, self.weather, self.distance, self.notes)

class Drone(db.Model):
    __tablename__ = "drones"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(25))
    model_id = db.Column(db.String(12))
