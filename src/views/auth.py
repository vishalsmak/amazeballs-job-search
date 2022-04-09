from flask import Blueprint, flash, redirect, render_template, url_for

from src.data.local_data import jobs
from src.forms.login import LoginForm
from src.forms.registration import RegistrationForm
from src.views.google_login import get_google_url

auth_app = Blueprint("auth", __name__)


@auth_app.route("/", methods=["GET"])
@auth_app.route("/home", methods=["GET"])
def home():
    return render_template("home.html", jobs=jobs)


@auth_app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("auth.home"))
    return render_template("register.html", title="Register", form=form)


@auth_app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (
            form.email.data == "admin@job.com"
            and form.password.data == "password"
        ):
            flash("You are logged in!", "success")
            return redirect(url_for("auth.home"))
        else:
            flash("Incorrect Login", "danger")
    return render_template(
        "login.html", title="Login", form=form, google_url=get_google_url()
    )


@auth_app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About")
