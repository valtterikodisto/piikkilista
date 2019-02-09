from application import db
from application.models import Base

from sqlalchemy.sql import text

class Organization(Base):

    name = db.Column(db.String(50), nullable=False)
    customers = db.relationship("Customer", backref='organization', lazy=True)

    def __init__(self, name):
        self.name = name

    def get_id():
        return self.id
    
    def get_amount_of_customers(self):
        stmt = text("SELECT COUNT(*) FROM customer"
                    " WHERE organization_id = :id").params(id=self.id)
        res = db.engine.execute(stmt)
        
        result = 0
        for row in res:
            result = row[0]
        
        return result

    def get_organization_balance(self):
        stmt = text("SELECT SUM(balance) FROM customer"
                    " WHERE organization_id = :id").params(id=self.id)
        
        res = db.engine.execute(stmt)

        result = 0
        for row in res:
            result = row[0]
        
        if not result:
            return 0.0
        else:
            return round((result/100),2)