from flask import flash, redirect, render_template, url_for

from src.app import app
from src.forms.login import LoginForm
from src.forms.registration import RegistrationForm
from src.local_data import jobs


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", jobs=jobs)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
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


@app.route("/about")
def about():
    return render_template("about.html", title="About")
