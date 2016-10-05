from flaskr import db
import datetime

class ETFOrder(db.Model):

    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    ext = db.Column(db.DateTime, default=datetime.datetime.now)
    amount = db.Column(db.Integer, nullable = False)
    price = db.Column(db.Integer, nullable=False)

    def __init__(self, amount, price):
        self.amount = amount
        self.price = price

    def __repr__(self):
        return '[%d, %d]'.format( self.amount, self.price)