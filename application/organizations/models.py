from application import db
from application.models import Base

class Organization(Base):

    name = db.Column(db.String(50), nullable=False)
    customers = db.relationship("Customer", backref='organization', lazy=True)

    def __init__(self, name):
        self.name = name