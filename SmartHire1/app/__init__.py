from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from ResumeParser import DBConnect

app = Flask(__name__)
smarthire_app = app

app.config['SECRET_KEY'] = 'f0c23d880346d1ef4f61655511699260'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

import app.routes

print(app)