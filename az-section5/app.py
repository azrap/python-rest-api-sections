from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)

api = Api(app)

items = []
# resource can be accessed with a GET method


class Item(Resource):
    parser = reqparse.RequestParser()

    # reqparse lets u specify things you want to go in the body and no other things
    parser.add_argument('price', type=float, required=True,
                        help="This field cannot be left blank!")

    def get(self, name):
        # search items, return x if x['name'] is name, or return None
        # next gets the first item (or None if returns None)

        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': None}, 200 if item is not None else 404

    def post(self, name):

        # if the item with that name already exists in items
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {"message": f'an item with name {name} already exists'}, 400

        # else create the item:
        data = Item.parser.parse_args()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        # specifying that we want to use the global items variable
        global items
        # filter x
        items = list(filter(lambda x: x['name'] != name, items))
        return {"message": "Item deleted"}

    def put(self, name):

        # parses the arguments and puts the valid ones in data (eg price in this case)
        data = Item.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price': data['price']}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):
    def get(self):
        return {'items': items}


# this is how you do it without the decorater
# localhost:5000/item/chair
api.add_resource(Item, '/item/<string:name>')

# localhost:5000/items
api.add_resource(ItemList, '/items')

# if missing, defaults to 5000
app.run(port=5000, debug=True)
