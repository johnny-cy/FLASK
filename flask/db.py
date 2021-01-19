from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)


# create a table by creating a class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    data_created = db.Column(db.DateTime, default=datetime.now)

class UserLevel(db.Model):
    # __tablename__ = 'UserLevelTable'
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(10))
    data_created = db.Column(db.DateTime, default=datetime.now)
