from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from user import UserRegister
from item import Item, ItemList
from security import authenticate, identity
from datetime import timedelta

app = Flask(__name__)
# To allow flask propagating exception even if debug is set to false on app
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


# if we don't specify the below, it defaults to /auth as endpoint for login
app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate, identity)

# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(minutes=18000)


items = []


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# only the file that you run is supposed to be main
# if you don't put main, that means it's imported and we don't want to run it
if __name__ == '__main__':
    app.run(port=5000, debug=True)  # important to mention debug=True
