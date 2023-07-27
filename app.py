from flask import Flask, request, render_template, url_for, redirect
import os
from models.database import db
from models.customer import Customer
from models.item import Item
from models.order_item import OrderItem
from models.order import Order
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + os.environ.get('DB_USERNAME', '') + ':' + os.environ.get('DB_PASSWORD', '') +'@localhost/' + os.environ.get('DB_DATABASE', '')
db.init_app(app)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return "Hello world!"

@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer.query.all()
    return render_template('customer/get_customers.html', customers=customers)


@app.route('/customers/<int:customer_id>/edit', methods=['POST', 'GET'])
def edit_customer(customer_id):

    customer = Customer.query.get(customer_id)
    if not customer:
        return "Customer not found", 404
    
    if request.method == 'GET':
        return render_template('customer/edit_customer.html', customer=customer)

    customer.first_name = request.form['first_name']
    customer.last_name = request.form['last_name']
    customer.birthdate = request.form['birthdate']
    db.session.commit()

    return redirect(url_for('get_customers'))


@app.route('/customers/<int:customer_id>/delete', methods=['POST'])
def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return "Customer not found", 404
    
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('get_customers'))

@app.route('/customers/add', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birthdate = request.form['birthdate']

        new_customer = Customer(first_name=first_name, last_name=last_name, birthdate=birthdate)
        db.session.add(new_customer)
        db.session.commit()

        return redirect(url_for('get_customers'))

    return render_template('customer/add_customer.html')


@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return render_template('item/get_items.html', items=items)

@app.route('/items/<int:item_id>/edit', methods=['POST', 'GET'])
def edit_item(item_id):

    item = Item.query.get(item_id)
    if not item:
        return "Item not found", 404
    
    if request.method == 'GET':
        return render_template('item/edit_item.html', item=item)

    item.name = request.form['name']
    item.price = request.form['price']
    db.session.commit()

    return redirect(url_for('get_items'))

@app.route('/items/<int:item_id>/delete', methods=['POST'])
def delete_item(item_id):
    item = Item.query.get(item_id)
    if not item:
        return "Item not found", 404
    
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('get_items'))

@app.route('/items/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']

        new_item = Item(name=name, price=price)
        db.session.add(new_item)
        db.session.commit()

        return redirect(url_for('get_items'))

    return render_template('item/add_item.html')

@app.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return render_template('order/get_orders.html', orders=orders)

@app.route('/orders/<int:order_id>/edit', methods=['POST', 'GET'])
def edit_order(order_id):

    order = Order.query.get(order_id)
    if not order:
        return "Order not found", 404
    
    if request.method == 'GET':
        customers = Customer.query.all()
        return render_template('order/edit_order.html', order=order, customers=customers)

    order.date = request.form['date']
    order.customer_id = request.form['customer_id']
    db.session.commit()

    return redirect(url_for('get_orders'))

@app.route('/orders/<int:order_id>/delete', methods=['POST'])
def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return "Order not found", 404
    
    db.session.delete(order)
    db.session.commit()
    return redirect(url_for('get_orders'))

@app.route('/orders/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        date = request.form['date']
        customer_id = request.form['customer_id']

        new_order = Order(date=date, customer_id=customer_id)
        db.session.add(new_order)
        db.session.commit()

        return redirect(url_for('get_orders'))
    
    customers = Customer.query.all()
    if not customers:
        return "Must be at least one customer to be able to create an order", 404

    return render_template('order/add_order.html', customers=customers)

if (__name__ == '__main__'):
    app.run()