from models.database import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    order_item = db.relationship('OrderItem', back_populates='item', uselist=False)

    def __repr__(self):
        return f'<Item {self.name}>'

