from db import db

# each model signifies a table


class ItemModel(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        # because ItemModel is now an extension of db.Model, we get all its methods, like .query etc.
        print('name', name)
        return cls.query.filter_by(name=name).first()

        # the below is the old school way to do it
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name, ))
        # row = result.fetchone()
        # connection.commit()
        # connection.close()

        # if row:
        #     item = cls(*row)

        #     return item

    def save_to_db(self):
        # .session opens up a session in SQLalchemy. Can do multiple things before committing
        db.session.add(self)
        db.session.commit()

    # def insert(self):
        # sql connection:
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        # query = "INSERT INTO items VALUES (?,?)"
        # cursor.execute(query, (self.name, self.price))

        # connection.commit()
        # connection.close()

    def delete_from_db(self):
        # sql connection:
        db.session.delete(self)
        db.session.commit()
