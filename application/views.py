from flask import redirect, render_template, request, url_for
from application import app, db
from flask_login import login_required
from application.orders.forms import OrderForm
from application.organizations.models import Organization
from application.customers.models import Customer
from application.orders.models import Order, DrinkAmount, Drink

@app.route("/", methods = ["GET"])
@login_required
def home():
  available_organizations = Organization.query.all()
  organizations_list = [(o.id, o.name) for o in available_organizations]

  form = OrderForm()
  form.organization_id.choices = organizations_list

  message = None
  if 'message' in request.args:
    message = request.args['message']

  return render_template("index.html", form=form, birthday_visible=False, message=message)


@app.route("/", methods=["POST"])
@login_required
def create_order():
  form = OrderForm(request.form)
  available_organizations = Organization.query.all()
  form.organization_id.choices = [(o.id, o.name) for o in available_organizations]

  if not form.validate():
    print(form.errors)
    return render_template("index.html", form=form, birthday_visible=False, error="Lomakkeen validointi ei onnistunut.")
  
  first_name = form.first_name.data.lower()
  last_name = form.last_name.data.lower()
  birthday = form.birthday.data
  organization_id = form.organization_id.data

  customers = None

  # There could be multiple customers in the same organization with the same name
  if birthday:
    customers = Customer.query.filter_by(first_name=first_name, last_name=last_name, birthday=birthday, organization_id=organization_id).all()
  else:
    customers = Customer.query.filter_by(first_name=first_name, last_name=last_name, organization_id=organization_id).all()

  # Handle invalid customer details
  if not customers:
    return render_template("index.html", form=form, birthday_visible=False, error="Käyttäjää ei löytynyt. Tarkista antamasi tiedot.")
  elif len(customers) > 1:
    return render_template("index.html", form=form, birthday_visible=True, error="Usealla jäsenellä tässä järjestössä on sama nimi. Anna myös syntymäpäivä.")

  # Get drinks and if there is none, generate them
  drinks = Drink.query.all()
  if not drinks:
    Drink.generate()
    drinks = Drink.query.all()

  print(drinks)

  drinkData = [
    form.beer.data,
    form.long_drink.data,
    form.cider.data,
    form.soft_drink.data,
    form.special_beer.data,
    form.drink.data,
    form.special_drink.data
  ]

  customer = customers[0]
  print('Customer:', customer)
  order = Order(customer.id)
  db.session.add(order)
  db.session.commit()
  order.add_drinks(drinks, drinkData)
  # db.session.begin_nested()
  # db.session.add(order)

  # try:
  #   i = 0
  #   total = 0
  #   while i < len(drinks):
  #     drink_id = drinks[i].id
  #     price = drinkData[i]*drinks[i].price
  #     drinkAmount = DrinkAmount(order.id, drink_id, drinkData[i])
  #     drinkAmount.drink = drinks[i]
  #     db.session.add(drinkAmount)
  #     total += price
  #     i += 1

  #   order.total = total
  #   db.session.commit()
  # except:
  #   db.session.rollback()
  # #finally:
  #   #db.session.close()
  
  # print('Order', order)
  # print('Drinks:')
  # for amount_drink in order.drinks:
  #   print('Amount', amount_drink.amount)
  #   print('Drink', amount_drink.drink.name)

  return redirect(url_for('home', message="Ostos lisätty asiakkaalle"))