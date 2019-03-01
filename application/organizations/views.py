from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.organizations.models import Organization
from application.organizations.forms import OrganizationForm

@app.route("/organizations/new")
@login_required(role="ADMIN")
def organizations_form():
    return render_template("organizations/new.html", form=OrganizationForm())

@app.route("/organizations", methods=["GET"])
@login_required(role="ANY")
def organizations_index():
    return render_template("organizations/list.html", organizations=Organization.query.all())

@app.route("/organizations", methods=["POST"])
@login_required(role="ADMIN")
def organizations_create():
    form = OrganizationForm(request.form)
    print(form.validate())

    if not form.validate():
        return render_template("organizations/new.html", form=form)

    new_organization = Organization(form.name.data, int(form.limit.data * 100))
    
    db.session.add(new_organization)
    db.session.commit()

    return redirect(url_for('organizations_index'))

@app.route("/organizations/<int:organization_id>", methods=["GET"])
@login_required(role="ADMIN")
def organizations_details(organization_id):
    organization = Organization.query.get_or_404(organization_id)
    form = OrganizationForm()

    return render_template("/organizations/details.html", organization=organization, form=form)

@app.route("/organizations/<int:organization_id>", methods=["POST"])
@login_required(role="ADMIN")
def organizations_update(organization_id):
    organization = Organization.query.get_or_404(organization_id)
    form = OrganizationForm(request.form)

    if not form.validate():
        return render_template("/organizations/details.html", organization=organization, form=form)

    organization.name = form.name.data
    organization.limit = int(form.limit.data * 100)

    db.session.commit()
    return redirect(url_for("organizations_details", organization_id=organization_id))

@app.route("/organizations/delete/<int:organization_id>", methods=["POST"])
@login_required(role="ADMIN")
def organizations_delete(organization_id):
    organization = Organization.query.get_or_404(organization_id)
    db.session.delete(organization)
    db.session.commit()

    return redirect(url_for("organizations_index"))