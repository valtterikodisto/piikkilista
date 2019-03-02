from application import app, db, login_required
from flask import redirect, render_template, request, url_for

from application.orders.models import Drink
from application.orders.forms import DrinkForm

@app.route("/drinks", methods=["GET"])
@login_required(role="ADMIN")
def drinks_form():
  drinks = Drink.query.order_by(Drink.id).all()
  form = DrinkForm()
  return render_template("drinks/edit.html", drinks=drinks, form=form)

@app.route("/drinks/<int:drink_id>", methods=["POST"])
@login_required(role="ADMIN")
def drinks_update(drink_id):
  form = DrinkForm(request.form)
  if (not form.validate()):
    drinks = Drink.query.order_by(Drink.id).all()
    return render_template("drinks/edit.html", drinks=drinks)

  drink = Drink.query.get_or_404(drink_id)
  drink.price = int(form.price.data * 100)
  db.session.commit()

  return redirect(url_for('drinks_form'))