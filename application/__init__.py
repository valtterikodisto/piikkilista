from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///piikkilista.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from application.customers import models, views
from application.organizations import models, views


db.create_all()