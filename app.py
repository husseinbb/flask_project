from flask import Flask, request, render_template, url_for, redirect
import os
from models.database import db
from models.customer import Customer
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
    return render_template('get_customer.html', customers=customers)


@app.route('/customers/<int:customer_id>/edit', methods=['POST', 'GET'])
def edit_customer(customer_id):

    customer = Customer.query.get(customer_id)
    if not customer:
        return "Customer not found", 404
    
    if request.method == 'GET':
        return render_template('edit_customer.html', customer=customer)

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

    return render_template('add_customer.html')


if (__name__ == '__main__'):
    app.run()