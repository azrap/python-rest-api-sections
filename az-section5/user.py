import sqlite3
from flask_restful import Resource, reqparse


# this is the equivalent of the data-model file in node.js


class User(object):
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

     # instead of hardcoding User, we use the cls/classmethod
    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"

        # cursor.execute accepts tuples only.
        # remember to put it in a tuple if it's one paramemter
        result = cursor.execute(query, (username,))

        # fetch the first one
        row = result.fetchone()

        if row:
            # cls = User here.
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


# it's a resource
class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="username field cannot be left blank!")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="password field cannot be left blank!"
                        )
    # gets called when we want to post user registration

    @classmethod
    def post(cls):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        data = cls.parser.parse_args()

        # id, username, password. ID is autoincremmenting so no need to put anything so null is fine

        query = "INSERT INTO users VALUES (NULL, ?, ? )"

        cursor.execute(query, (data['username'], data['password'], ))
        connection.commit()
        connection.close()
        return {"message": "User created successfully."}, 201
