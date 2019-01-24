from application import db
from datetime import datetime

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    blocks = db.relationship("Block", backref='customer', lazy=True, order_by="desc(Block.date_end)")
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)

    def __init__(self, first_name, last_name, birthday, balance, organization_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.balance = balance
        self.organization_id = organization_id

    def get_balance_in_euros(self):
        balance_in_euros = self.balance / 100
        return round(balance_in_euros, 2)

    def get_block_status(self):
        if (self.blocks):
            return self.blocks[0].date_end > datetime.now()
        else:
            return False

    def serialize(self):  
        return {
            'id': self.id,
            'organization_id': self.organization_id,
            'block': self.get_block_status(),
            'first_name': self.first_name, 
            'last_name': self.last_name,
            'birthday': self.birthday,
            'balance': self.balance,
        }

class Block(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    date_start = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_end = db.Column(db.DateTime, nullable=False)

    def __init__(self, customer_id, date_end):
        self.customer_id = customer_id
        self.date_end = date_end