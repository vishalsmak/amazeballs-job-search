from flask import Blueprint, flash, redirect, render_template, url_for

from src.forms.login import LoginForm
from src.forms.registration import RegistrationForm
from src.local_data import jobs

auth_app = Blueprint("auth", __name__)


@auth_app.route("/auth/home", methods=["GET"])
def home():
    return render_template("home.html", jobs=jobs)


@auth_app.route("/auth/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@auth_app.route("/auth/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (
            form.email.data == "admin@job.com"
            and form.password.data == "password"
        ):
            flash("You are logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Incorrect Login", "danger")
    return render_template("login.html", title="Login", form=form)


@auth_app.route("/auth/about", methods=["GET"])
def about():
    return render_template("about.html", title="About")
