from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from market.config import prod_DB, web_DB

import os



app = Flask(__name__)


#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

if os.environ.get('DEBUG') == '1':
    app.config['SQLALCHEMY_DATABASE_URI'] = web_DB
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = prod_DB
     
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes
