from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)

api = Api(app)

items = []
# resource can be accessed with a GET method


class Item(Resource):
    def get(self, name):
        # search items, return x if x['name'] is name, or return None
        # next gets the first item (or None if returns None)

        item = next(filter(lambda x: x['name'] == name, items), None)
        return {'item': None}, 200 if item is not None else 404
    # def get(self, name):
    #     for item in items:
    #         if name == item['name']:
    #             return item, 200

        # if item doesn't exist
        # return {'item': None}, 404

    def post(self, name):
        # if the item with that name already exists in items
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {"message": f'an item with name {name} already exists'}, 400

        # else create the item:
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201

    def delete(self, name):
        pass


class ItemList(Resource):
    def get(self):
        return {'items': items}


# this is how you do it without the decorater
# localhost:5000/student/Rolf
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

# if missing, defaults to 5000
app.run(port=5000, debug=True)
