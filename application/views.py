from flask import redirect, render_template, request, url_for
from application import app, db
from flask_login import login_required
from application.orders.forms import OrderForm
from application.organizations.models import Organization
from application.customers.models import Customer
from application.orders.models import Order, DrinkAmount, Drink

# Home page

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

# Handles POST for adding new orders

@app.route("/", methods=["POST"])
@login_required
def create_order():
  form = OrderForm(request.form)
  available_organizations = Organization.query.all()
  form.organization_id.choices = [(o.id, o.name) for o in available_organizations]

  if not form.validate():
    print(form.errors)
    return render_template("index.html", form=form, birthday_visible=False, error="Lomakkeen validointi ei onnistunut.")
  
  first_name = form.first_name.data.lower().capitalize()
  last_name = form.last_name.data.lower().capitalize()
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

  customer = customers[0]
  if not customer.can_purchase(form.deposit.data):
    return render_template("index.html", form=form, birthday_visible=False, error="Asiakkaan tulee maksaa piikki pois eston poistamiseksi (%.2f €)" % customer.get_balance_in_euros())
  
  if customer.get_block_status():
    return render_template("index.html", form=form, birthday_visible=False, error="Asiakas on estetty.")

  # Get drinks and if there is none, generate them
  drinks = Drink.query.all()
  if not drinks:
    Drink.generate()
    drinks = Drink.query.all()

  drinkData = [
    form.beer.data,
    form.long_drink.data,
    form.cider.data,
    form.soft_drink.data,
    form.special_beer.data,
    form.drink.data,
    form.special_drink.data,
    form.whisky.data
  ]

  order = Order(customer.id)
  db.session.add(order)
  db.session.commit()

  # Add drinks to the order
  order.add_drinks(customer, drinks, drinkData, form.deposit.data)

  return redirect(url_for('home', message="Ostos lisätty asiakkaalle. Asiakkaan piikki on nyt %.2f €"%customer.get_balance_in_euros()))