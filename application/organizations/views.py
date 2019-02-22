from application import app, db, login_manager
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application.organizations.models import Organization
from application.organizations.forms import OrganizationForm

@app.route("/organizations/new")
@login_required
def organizations_form():
    if not current_user.is_admin():
        return login_manager.unauthorized()
    return render_template("organizations/new.html", form=OrganizationForm())

@app.route("/organizations", methods=["GET"])
@login_required
def organizations_index():
    return render_template("organizations/list.html", organizations=Organization.query.all())

@app.route("/organizations", methods=["POST"])
@login_required
def organizations_create():
    if not current_user.is_admin():
        return login_manager.unauthorized()
        
    form = OrganizationForm(request.form)
    print(form.validate())

    if not form.validate():
        return render_template("organizations/new.html", form=form)

    new_organization = Organization(form.name.data, int(form.limit.data * 100))
    
    db.session.add(new_organization)
    db.session.commit()

    return redirect(url_for('organizations_index'))