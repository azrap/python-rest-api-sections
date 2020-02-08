import sqlite3
from db import db


# each model will be an extension of db.Model class
class UserModel(db.Model):

    # tell SQLAlchemy where the model will be stored
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    # define the schema for each column
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password
        self.something = "hi"

     # instead of hardcoding User, we use the cls/classmethod
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
