from models.database import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

    item = db.relationship('OrderItem', back_populates='order', uselist=False)

    def __repr__(self):
        return f'<Order {self.id}>'

