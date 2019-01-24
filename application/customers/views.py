from application import app, db
from flask import redirect, render_template, request, url_for, jsonify
from application.customers.models import Customer, Block
from application.organizations.models import Organization
from application.customers.forms import CustomerForm, CustomerBlockForm
from datetime import datetime

# Page for adding new customers

@app.route("/customers/new")
def customers_form():
    available_organizations = Organization.query.all()
    organizations_list = [(o.id, o.name) for o in available_organizations]
    form = CustomerForm()
    form.organization_id.choices = organizations_list

    return render_template("customers/new.html", form=form)

# Page for indexing customers

@app.route("/customers", methods=["GET"])
def customers_index():
    return render_template("customers/list.html", customers=Customer.query.all())

# Handles POST requests for adding a new customer

@app.route("/customers", methods=["POST"])
def customers_create():
    form = CustomerForm(request.form)
    available_organizations = Organization.query.all()
    form.organization_id.choices = [(o.id, o.name) for o in available_organizations]    

    if not form.validate():
        return render_template("customers/new.html", form=form)

    new_customer = Customer (
        form.first_name.data,
        form.last_name.data,
        form.birthday.data,
        form.balance.data,
        form.organization_id.data
    )

    db.session().add(new_customer)
    db.session().commit()

    return redirect(url_for("customers_index"))

# Page for customer overview

@app.route("/customers/<int:customer_id>", methods=["GET"])
def customers_details(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    user_block = Block.query.filter(Block.customer_id == customer_id).filter(Block.date_end >= now).order_by(Block.date_end.desc()).first()

    form = CustomerForm()
    available_organizations = Organization.query.all()
    organizations_list = [(o.id, o.name) for o in available_organizations]
    form.organization_id.choices = organizations_list

    block_form = CustomerBlockForm()

    return render_template("/customers/details.html", customer=customer, form=form, visibility="hidden", user_block=user_block, block_form=block_form)

# Handles POST requests for customer update

@app.route("/customers/<int:customer_id>", methods=["POST"])
def customers_update(customer_id):
    form = CustomerForm(request.form)
    customer = Customer.query.get_or_404(customer_id)
    available_organizations = Organization.query.all()
    form.organization_id.choices = [(o.id, o.name) for o in available_organizations]

    if not form.validate():
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        user_block = Block.query.filter(Block.customer_id == customer_id).filter(Block.date_end >= now).order_by(Block.date_end.desc()).first()

        return render_template("/customers/details.html", customer=customer, form=form, visibility="visible", user_block=user_block, block_form=CustomerBlockForm())

    customer.first_name = form.first_name.data
    customer.last_name = form.last_name.data
    customer.birthday = form.birthday.data
    customer.balance = form.balance.data
    customer.organization_id = form.organization_id.data

    db.session().commit()

    return redirect(url_for("customers_details", customer_id=customer_id))

# Handles POST requests for blocking a customer

@app.route("/customers/block/<int:customer_id>", methods=["POST"])
def customers_block(customer_id):
    form = CustomerBlockForm(request.form)

    if not form.validate():
        customer = Customer.query.get_or_404(customer_id)
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        user_block = Block.query.filter(Block.customer_id == customer_id).filter(Block.date_end >= now).order_by(Block.date_end.desc()).first()
        return render_template("/customers/details.html", customer=customer, user_block=user_block, form=form)

    new_block = Block (
        customer_id,
        form.date_end.data
    )

    db.session().add(new_block)
    db.session.commit()
    
    return redirect(url_for("customers_details", customer_id=customer_id))

# JSON data for front page customer firsname & lastname autocomplete

@app.route("/customers/json")
def customers_json():
    available_customers = Customer.query.all()
    customers = [c.serialize for c in available_customers]
    return jsonify(customers_list=[c.serialize() for c in Customer.query.all()])