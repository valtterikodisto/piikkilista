from application import db
from application.models import Base

from sqlalchemy.sql import text

class Organization(Base):

    name = db.Column(db.String(50), nullable=False)
    limit = db.Column(db.Integer, nullable=False)
    customers = db.relationship("Customer", cascade="all,delete", backref='organization', lazy=True)

    def __init__(self, name, limit):
        self.name = name
        self.limit = limit

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

    def get_average_order_total(self):
        stmt = text("SELECT AVG(purchase.total) AS average FROM organization"
                    " INNER JOIN customer ON customer.organization_id = organization.id"
                    " INNER JOIN purchase ON purchase.customer_id = customer.id"
                    " WHERE organization_id = :id").params(id=self.id)

        res = db.engine.execute(stmt)
        result = res.fetchone()
        if not result['average']:
            return 0.0
        else:
            return round(float(result['average']) / 100, 2)

    def get_limit(self):
        return round(self.limit/100, 2)