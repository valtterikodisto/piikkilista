from application import app, db, login_required
from flask import redirect, render_template, request, url_for, jsonify
from flask_login import current_user

from application.customers.models import Customer, Block
from application.organizations.models import Organization
from application.orders.models import Order
from application.customers.forms import CustomerForm, CustomerBlockForm

from datetime import datetime

# Page for adding new customers

@app.route("/customers/new")
@login_required(role="ADMIN")
def customers_form():
    available_organizations = Organization.query.all()
    organizations_list = [(o.id, o.name) for o in available_organizations]
    form = CustomerForm()
    form.organization_id.choices = organizations_list

    return render_template("customers/new.html", form=form)

# Page for indexing customers

@app.route("/customers", methods=["GET"])
@login_required(role="ANY")
def customers_index():
    page = request.args.get('page', 1, type=int)
    first_name = request.args.get('first_name', '', type=str)
    last_name = request.args.get('last_name', '', type=str)

    customers = Customer.query.filter(Customer.first_name.ilike("%"+first_name+"%")).filter(Customer.last_name.ilike("%"+last_name+"%")).order_by(Customer.organization_id).paginate(page=page, per_page=10)
    return render_template("customers/list.html", customers=customers, first_name=first_name, last_name=last_name)

# Handles POST requests for adding a new customer

@app.route("/customers", methods=["POST"])
@login_required(role="ADMIN")
def customers_create():
    form = CustomerForm(request.form)
    available_organizations = Organization.query.all()
    form.organization_id.choices = [(o.id, o.name) for o in available_organizations]    

    if not form.validate():
        return render_template("customers/new.html", form=form)

    new_customer = Customer (
        form.first_name.data.lower().capitalize(),
        form.last_name.data.lower().capitalize(),
        form.birthday.data,
        int(round(form.balance.data * 100, 2)),
        form.organization_id.data
    )

    db.session().add(new_customer)
    db.session().commit()

    return redirect(url_for("customers_index"))

# Page for customer overview

@app.route("/customers/<int:customer_id>", methods=["GET"])
@login_required(role="ADMIN")
def customers_details(customer_id):
    page = request.args.get('page', 1, type=int)
    customer = Customer.query.get_or_404(customer_id)
    orders = Order.query.filter(Order.customer_id == customer.id).order_by(Order.date_created.desc()).paginate(page=page, per_page=8)
    block_end_date = customer.get_block_status()

    form = CustomerForm()
    available_organizations = Organization.query.all()
    organizations_list = [(o.id, o.name) for o in available_organizations]
    form.organization_id.choices = organizations_list

    block_form = CustomerBlockForm()

    return render_template("/customers/details.html", customer=customer, orders=orders, form=form, visibility="hidden", block_end_date=block_end_date, block_form=block_form)

# Handles POST requests for customer update

@app.route("/customers/<int:customer_id>", methods=["POST"])
@login_required(role="ADMIN")
def customers_update(customer_id):
    page = request.args.get('page', 1, type=int)
    form = CustomerForm(request.form)
    customer = Customer.query.get_or_404(customer_id)
    orders = Order.query.filter(Order.customer_id == customer.id).order_by(Order.date_created.desc()).paginate(page=page, per_page=8)
    available_organizations = Organization.query.all()
    form.organization_id.choices = [(o.id, o.name) for o in available_organizations]

    if not form.validate():
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_block = Block.query.filter(Block.customer_id == customer_id).filter(Block.date_end >= now).order_by(Block.date_end.desc()).first()
        block_form = CustomerBlockForm()
        block_end_date = customer.get_block_status()

        return render_template("/customers/details.html", customer=customer, orders=orders, form=form, visibility="visible", block_end_date=block_end_date, user_block=user_block, block_form=block_form)

    customer.first_name = form.first_name.data.lower().capitalize()
    customer.last_name = form.last_name.data.lower().capitalize()
    customer.birthday = form.birthday.data
    customer.balance = int(round(form.balance.data * 100, 2))
    customer.organization_id = form.organization_id.data

    db.session().commit()

    return redirect(url_for("customers_details", customer_id=customer_id))

# Handles POST requests for blocking a customer

@app.route("/customers/block/<int:customer_id>", methods=["POST"])
@login_required(role="ADMIN")
def customers_block(customer_id):
    form = CustomerBlockForm(request.form)

    if not form.validate():
        customer = Customer.query.get_or_404(customer_id)
        block_end_date = customer.get_block_status()
        user_block = Block.query.filter(Block.customer_id == customer_id).filter(Block.date_end >= now).order_by(Block.date_end.desc()).first()

        page = request.args.get('page', 1, type=int)
        orders = Order.query.filter(Order.customer_id == customer.id).order_by(Order.date_created.desc()).paginate(page=page, per_page=8)

        return render_template("/customers/details.html", customer=customer, orders=orders, user_block=user_block, block_end_date=block_end_date, form=form)

    new_block = Block (
        customer_id,
        form.date_end.data
    )

    db.session().add(new_block)
    db.session.commit()
    
    return redirect(url_for("customers_details", customer_id=customer_id))

# Handles customer deletion

@app.route("/customers/delete/<int:customer_id>", methods=["POST"])
@login_required(role="ADMIN")
def customers_delete(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()

    return redirect(url_for("customers_index"))

@app.route("/customers/search", methods=["POST"])
@login_required(role="ANY")
def customers_search():
    first_name = request.form.get("first_name").strip()
    last_name = request.form.get("last_name").strip()
    customers = None

    if not first_name and not last_name:
        return redirect(url_for('customers_index'))

    return redirect(url_for('customers_index', first_name=first_name, last_name=last_name))

# JSON data for front page customer firstname & lastname autocomplete

@app.route("/customers/json")
@login_required(role="ANY")
def customers_json():
    available_customers = Customer.query.all()
    customers = [c.serialize for c in available_customers]
    return jsonify(customers_list=[c.serialize() for c in Customer.query.all()])