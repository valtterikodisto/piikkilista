from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///piikkilista.db"
    app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application import views
from application.customers import models, views
from application.organizations import models, views

# login
app.config["SECRET_KEY"] = os.urandom(32)


db.create_all()