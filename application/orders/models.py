from application import db
from application.models import Base

from sqlalchemy.sql import text

class Order(Base):
  __tablename__ = 'purchase'
  customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
  total = db.Column(db.Integer)
  drinks = db.relationship("DrinkAmount")

  def __init__(self, customer_id):
    self.customer_id = customer_id

  def add_drinks(self, drinks, drinkData):
    db.session.begin_nested()
    db.session.add(self)

    total = 0
    i = 0
    try:
      while i < len(drinks)+1:
        price = drinkData[i] * drinks[i].price
        drinkAmount = DrinkAmount(self.id, drinks[i].id, drinkData[i])
        drinkAmount.drink = drinks[i]
        db.session.add(drinkAmount)
        total += price
        i += 1

      self.total = total
      db.session.commit()
      return True
    except:
      db.session.rollback()
    
    return False


class Drink(Base):
  name = db.Column(db.String(20))
  price = db.Column(db.Integer)

  def __init__(self, name, price):
    self.name = name
    self.price = price
  
  def generate():
    drinks = [{'olut':150}, {'lonkero':150}, {'siideri':150}, {'alkoholiton':100}, {'erikoisolut':250}, {'drinkki':250}, {'erikoisdrinkki':350}]
    for drink in drinks:
      for drinkName in drink:
        db.session.add(Drink(drinkName, drink.get(drinkName)))
        db.session.commit()

class DrinkAmount(db.Model):
  order_id = db.Column(db.Integer, db.ForeignKey('purchase.id'), primary_key=True)
  drink_id = db.Column(db.Integer, db.ForeignKey('drink.id'), primary_key=True)
  amount = db.Column(db.Integer)
  drink = db.relationship("Drink")

  def __init__(self, order_id, drink_id, amount):
    self.order_id = order_id
    self.drink_id = drink_id
    self.amount = amount