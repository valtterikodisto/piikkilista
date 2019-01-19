from application import app, db
from flask import redirect, render_template, request, url_for
from application.organizations.models import Organization
from application.organizations.forms import OrganizationForm

@app.route("/organizations/new")
def organizations_form():
    return render_template("organizations/new.html", form=OrganizationForm())

@app.route("/organizations", methods=["GET"])
def organizations_index():
    return render_template("organizations/list.html", organizations=Organization.query.all())

@app.route("/organizations", methods=["POST"])
def organizations_create():
    form = OrganizationForm(request.form)
    print(form.name.data)
    print(form.validate())

    if not form.validate():
        return render_template("organizations/new.html", form=form)

    new_organization = Organization(form.name.data)
    
    db.session.add(new_organization)
    db.session.commit()

    return redirect(url_for('organizations_index'))