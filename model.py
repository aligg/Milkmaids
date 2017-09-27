"""Model and database functions for Milkmaids"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Order(db.model):
    """Orders for website"""

    __tablename__ = "orders"

    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    order_status = db.Column(db.String(30))
    order_date = db.Column(db.DateTime)

    def __repr__(self):
        """Provide representation when printed"""

        return "<Order order_id=%s user_id=%s order_status=%s order_date=%s>" %(self.order_id, self.user_id, self.order_status, self.order_date)

class User(db.model):
    """Users of website"""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=True)
    username = db.Column(db.String(64), nullable=True)
    password = db.Column(db.String(64), nullable=True)
    address = db.Column(db.String(64), nullable=True)
    zipcode = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        """Provide representation when printed"""

        return "<User user_id=%s firstname=%s lastname=%s username=%s password=%s address=%s zipcode=%s email=%s>" %(self.user_id, self.firstname, self.lastname, self.username, self.password, self.address, self.zipcode, self.email)

class Milk(db.model):
    """Milk for website"""

    __tablename__ = "milk"

    milk_id = db.Column(db.Integer, primary_key=True)
    smoker = db.Column(db.bool)
    baby_age = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    price_per_oz = db.Column(db.Integer)
    inventory = db.Column(db.Integer)
    date = db.Column(db.datetime)

    def __repr__(self):
        """Provide representation when printed"""

        return "<Milk milk_id=%s smoker=%s baby_age=%s user_id=%s price_per_oz=%s inventory=%s date=%s>" %(self.milk_id, self.smoker, self.baby_age, self.user_id, self.price_per_oz, self.inventory, self.date)

class Order_item(db.model):
    """Items in Order"""

    __tablename__ = "order_items"

    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.order_id'))
    milk_id = db.Column(db.Integer, db.ForeignKey('milk.milk_id'))
    quantity = db.Column(db.Integer)

    def __repr__(self):
        """Provide representation when printed"""

        return "<Order_item>"
class Milk_diet(db.model):
    """Milk donated to milk website"""

    __tablename__ = "milk_diet"

    milk_diet_id = db.Column(db.Integer, primary_key=True)
    milk_id = db.Column(db.Integer(30), db.ForeignKey('milk.milk_id'))
    diet_id = db.Column(db.Integer(30), db.ForeignKey('diet.diet_id'))

    def __repr__(self):
        """Provide representation when printed"""


class Diet(db.model):
    """Stores diet information about milk"""

    __tablename__ = "diet"
    diet_id = db.Column(db.Integer, primary_key=True)
    diet_name = db.Column(db.String(64))

    def __repr__(self):
        """Provide representation when printed"""


#Helper functions


def connect_to_db(app):
    """"Connect the database to the flask app"""
