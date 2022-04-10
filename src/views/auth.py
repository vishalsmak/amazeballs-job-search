from flask import Blueprint, flash, redirect, render_template, url_for

from src.data.local_data import jobs
from src.forms.application import ApplicationForm
from src.forms.login import LoginForm
from src.forms.registration import RegistrationForm
from src.forms.search import SearchForm
from src.forms.updateaccount import UpdateAccountForm
from src.views.google_login import get_google_url

# from src.local_data import jobs


auth_app = Blueprint("auth", __name__)


@auth_app.route("/", methods=["GET"])
@auth_app.route("/land", methods=["GET"])
def landing():
    return render_template("landing.html", title="land")


@auth_app.route("/home", methods=["GET"])
def home():
    form = SearchForm()
    return render_template("home.html", jobs=jobs, form=form)


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


@auth_app.route("/profile", methods=["GET", "POST"])
def profile():
    return render_template("user_profile.html", title="Profile")


@auth_app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    return render_template("edit_profile.html", title="Edit profile")


@auth_app.route("/logout")
def logout():
    return redirect(url_for("auth.landing"))


@auth_app.route("/account", methods=["GET", "POST"])
def account():
    form = UpdateAccountForm()
    image_file = url_for("static", filename="profiling.jpg")
    return render_template(
        "profile.html", title="Account", image_file=image_file, form=form
    )


@auth_app.route("/apply", methods=["GET", "POST"])
def apply():
    form = ApplicationForm()
    return render_template("apply.html", title="Application", form=form)
