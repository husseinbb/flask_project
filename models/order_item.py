from models.database import db

class OrderItem(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)

    order = db.relationship('Order', back_populates='item', uselist=False)

    item = db.relationship('Item', back_populates='order_item', uselist=False)

    def __repr__(self):
        return f'<OrderItem {self.order_id}, {self.item_id}>'

