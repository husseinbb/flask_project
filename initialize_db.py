from models.customer import db as customer_db
from models.item import db as item_db
from models.order import db as order_db
from models.order_item import db as order_item_db
from app import app

def create_tables():
    with app.app_context():
        customer_db.create_all()
        item_db.create_all()
        order_db.create_all()
        order_item_db.create_all()

if __name__ == '__main__':
    create_tables()

