from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm
from flask_login import login_required

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, error = "Käyttäjänimi tai salasana oli väärä")

    login_user(user)
    return redirect(url_for("home"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("auth_login"))

@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())
    
    form = RegisterForm(request.form)

    if not form.validate():
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                print(err)
        return render_template("auth/registerform.html", form=form)

    user = User.query.filter_by(username=form.username.data).first()
    if user:
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                print(err)
        return render_template("auth/registerform.html", form = form, errorMessage = "Käyttäjänimi on jo käytössä")
    
    new_user = User (
        form.username.data,
        form.password.data,
        False
    )

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth_login"))