from flask import Flask
import os
from models.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123123@localhost/Neo'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://' + os.environ.get('DB_USERNAME', '') + ':' + os.environ.get('DB_PASSWORD', '') +'@localhost/' + os.environ.get('DB_DATABASE', '')
db.init_app(app)

@app.route('/')
def home():
    return "Hello world!"



if (__name__ == '__main__'):
    app.run()