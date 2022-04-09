from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user,login_user,logout_user

from src.forms.login import LoginForm
from src.forms.registration import RegistrationForm
from src.forms.updateaccount import UpdateAccountForm
from src.forms.application import ApplicationForm
from src.local_data import jobs

auth_app = Blueprint("auth", __name__)


@auth_app.route("/", methods=["GET"])
@auth_app.route("/land", methods=["GET"])
def landingpg():
    return render_template("landingpg.html",title="land")

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
    return render_template("login.html", title="Login", form=form)


@auth_app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", title="About")

@auth_app.route("/profile", methods=["GET", "POST"])
def profile():
    return render_template("userprofile.html", title="Profile")

@auth_app.route("/editprofile", methods=["GET", "POST"])
def editprofile():
    return render_template("editprofile.html", title="Edit profile")

@auth_app.route("/logout")
def logout():
    #logout_user()
    return redirect(url_for('auth.landingpg'))

@auth_app.route("/account", methods=['GET', 'POST'])
def account():
    form = UpdateAccountForm()
    image_file= url_for('static',filename='profileimg.jpg')
    return render_template('profile.html', title='Account', image_file= image_file, form=form)

@auth_app.route("/apply", methods=['GET', 'POST'])
def apply():
    form = ApplicationForm()
    return render_template('apply.html', title='Application', form=form)
