import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
app = Flask(__name__)

app.config['SECRET_KEY'] = '0b6bd163c27f7d7512077a91'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'abigail.nyawira22@gmail.com'
app.config['MAIL_PASSWORD'] = 'WaChIrA07!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
db = SQLAlchemy(app)
db.create_all()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from app import main

