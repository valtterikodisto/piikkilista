from application import db
from application.models import Base

from sqlalchemy.sql import text

class Order(Base):
  __tablename__ = 'purchase'
  customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('account.id'))
  total = db.Column(db.Integer)
  deposit = db.Column(db.Integer)
  drinks = db.relationship("DrinkAmount")

  def __init__(self, customer_id, user_id):
    self.customer_id = customer_id
    self.user_id  = user_id

  def get_total_in_euros(self):
    return round(self.total/100, 2)

  def get_deposit_in_euros(self):
    return round(self.deposit/100, 2)

  def add_drinks(self, customer, drinks, drinkData, deposit):
    db.session.add(self)
    db.session.add(customer)

    total = 0
    i = 0
    while i < len(drinks):
      price = drinkData[i] * drinks[i].price
      drinkAmount = DrinkAmount(self.id, drinks[i].id, int(drinkData[i]))
      drinkAmount.drink = drinks[i]
      db.session.add(drinkAmount)
      db.session.commit()
      total += price
      i += 1

    self.total = total
    self.deposit = int(round(deposit * 100, 2))
    customer.balance -= total-self.deposit
    db.session.commit()


class Drink(Base):
  name = db.Column(db.String(20))
  price = db.Column(db.Integer)

  def __init__(self, name, price):
    self.name = name
    self.price = price
  
  def generate():
    # Default values for drinks
    drinks = [{'olut':150}, {'lonkero':150}, {'siideri':150}, {'alkoholiton':100}, {'erikoisolut':250}, {'drinkki':250}, {'erikoisdrinkki':350}, {'viski':400}]
    for drink in drinks:
      for drinkName in drink:
        db.session.add(Drink(drinkName, drink.get(drinkName)))
        db.session.commit()

  def get_price_in_euros(self):
    return round(self.price/100, 2)

class DrinkAmount(Base):
  order_id = db.Column(db.Integer, db.ForeignKey('purchase.id'))
  drink_id = db.Column(db.Integer, db.ForeignKey('drink.id'))
  amount = db.Column(db.Integer)
  drink = db.relationship("Drink")

  def __init__(self, order_id, drink_id, amount):
    self.order_id = order_id
    self.drink_id = drink_id
    self.amount = amount