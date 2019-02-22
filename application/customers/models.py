from application import db
from datetime import datetime
from application.models import Base
from application.organizations.models import Organization

from sqlalchemy.sql import text

class Customer(Base):

    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    blocks = db.relationship("Block", backref='customer', lazy=True, order_by="desc(Block.date_end)")
    orders = db.relationship("Order", backref='customer', lazy=True)
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

    def can_purchase(self, deposit):
        limit = Organization.query.filter_by(id=self.organization_id).first().limit
        return self.balance >= -1 * limit or int(round(deposit * 100, 2)) >= -1 * self.balance

    def get_block_status(self):
        now = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        stmt = text("SELECT block.date_end FROM block"
                    " WHERE block.customer_id = :id"
                    " AND block.date_end > :current"
                    " ORDER BY block.date_end DESC").params(id=self.id, current=now)
        
        res = db.engine.execute(stmt)
        result = res.fetchone()
        if not result:
            return None
        else:
            import os
            if os.environ.get("HEROKU"):
                return result['date_end']
            else:
                date = datetime.strptime(result['date_end'].split('.')[0], '%Y-%m-%d %H:%M:%S')
                return date.strftime('%Y-%m-%d %H:%M')
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