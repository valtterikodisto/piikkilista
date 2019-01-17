from application import app, db
from flask import redirect, render_template, request, url_for
from application.organizations.models import Organization

@app.route("/organizations/new")
def organizations_form():
    return render_template("organizations/new.html")

@app.route("/organizations", methods=["GET"])
def organizations_index():
    return render_template("organizations/list.html", organizations=Organization.query.all())

@app.route("/organizations", methods=["POST"])
def organizations_create():
    new_organization = Organization (
        request.form.get("name")
    )
    
    db.session.add(new_organization)
    db.session.commit()

    return redirect(url_for('organizations_index'))