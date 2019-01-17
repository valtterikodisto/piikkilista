from application import app, db
from flask import redirect, render_template, request, url_for
from application.customers.models import Customer
from application.organizations.models import Organization

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
def customer_details(customer_id):
    customer = Customer.query.get(customer_id)

    return render_template("/customers/details.html", customer=customer)

