from application import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    organization_id = db.Column(db.Integer, db.ForeignKey('organization.id'), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Integer, nullable=False)
    balance = db.Column(db.Integer, nullable=False)

    def __init__(self, first_name, last_name, birthday, organization_id, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.balance = balance
        self.organization_id = organization_id

    def get_balance_in_euros(self):
        balance_in_euros = self.balance / 100
        return round(balance_in_euros, 2)