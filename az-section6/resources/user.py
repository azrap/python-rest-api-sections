import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

# this is the equivalent of the data-model file in node.js


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

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        # id, username, password. ID is autoincremmenting so no need to put anything so null is fine        select_query = f"SELECT * FROM users where username={data['username']}"

        query = "INSERT INTO users VALUES (NULL, ?, ? )"
        cursor.execute(query, (data['username'], data['password'], ))

        connection.commit()
        connection.close()
        return {"message": "User created successfully."}, 201
