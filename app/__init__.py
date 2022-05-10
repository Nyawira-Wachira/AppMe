from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '0b6bd163c27f7d7512077a91'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from app import main

