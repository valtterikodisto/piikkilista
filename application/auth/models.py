from application import db
from application.models import Base

class User(Base):

    __tablename__ = "account"

    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    orders = db.relationship("Order", backref="account")

    def __init__(self, username, password, admin):
        self.username = username
        self.password = password
        self.admin = admin
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
    
    def is_admin(self):
        return self.admin

    def roles(self):
        if (self.admin):
            return ["ADMIN"]
        else:
            return ["USER"]