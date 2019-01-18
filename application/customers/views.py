from application import app, db
from flask import redirect, render_template, request, url_for
from application.customers.models import Customer, Block
from application.organizations.models import Organization
from datetime import datetime

@app.route("/customers/new")
def customers_form():
    return render_template("customers/new.html",  organizations=Organization.query.all())

@app.route("/customers", methods=["GET"])
def customers_index():
    return render_template("customers/list.html", customers=Customer.query.all())

@app.route("/customers", methods=["POST"])
def customers_create():
    # Here we need to validate user input

    new_customer = Customer (
        request.form.get("first_name"),
        request.form.get("last_name"),
        request.form.get("birthday"),
        request.form.get("organization_id"),
        request.form.get("balance")
    )

    db.session().add(new_customer)
    db.session().commit()

    return redirect(url_for("customers_index"))

@app.route("/customers/<int:customer_id>", methods=["GET"])
def customers_details(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    user_block = Block.query.filter_by(customer_id=customer.id).order_by(Block.date_end.desc()).first()

    return render_template("/customers/details.html", customer=customer, user_block=user_block)

@app.route("/customers/block/<int:customer_id>", methods=["POST"])
def customers_block(customer_id):

    # Here we need to validate user input
    new_block = Block (
        customer_id,
        datetime.strptime(request.form.get("date_end"), '%Y-%m-%d')
    )

    db.session().add(new_block)
    db.session.commit()

    return redirect(url_for("customers_details", customer_id=customer_id))