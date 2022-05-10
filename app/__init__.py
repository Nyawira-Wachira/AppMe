# import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from alembic import op
import sqlalchemy as sa
app = Flask(__name__)

app.config['SECRET_KEY'] = '0b6bd163c27f7d7512077a91'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///account.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db, render_as_batch=True)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'


from app import main

