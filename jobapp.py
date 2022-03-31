from flask import Flask, flash, redirect, render_template, url_for

from forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "53070fbaabd54efe45ed035a467ecc3f"

jobs = [
    {
        "company": "Microsoft",
        "job_title": "Graduate Software Engineer",
        "location": "London",
        "date_posted": "January 10, 2022",
        "apply_till": "March 30, 2022",
        "about": "Responsibilities: sfjnkjnk,jnnnnn",
        "apply_here": "Apply here",
    },
    {
        "company": "Deutsche Bank",
        "job_title": "Graduate Software Engineer",
        "location": "London",
        "date_posted": "January 10, 2022",
        "apply_till": "March 30, 2022",
        "about": "Responsibilities: sfjnkjnk,jnnns",
        "apply_here": "Apply here",
    },
    {
        "company": "Facebook",
        "job_title": "Junior Support Analyst",
        "location": "Remote",
        "date_posted": "February 7, 2022",
        "apply_till": "April 12, 2022",
        "about": "Responsibilities: sfjnkjnk,jnnns",
        "apply_here": "Apply here",
    },
    {
        "company": "Capgemini",
        "job_title": "Junior Network Analyst",
        "location": "Brighton",
        "date_posted": "February 7, 2022",
        "apply_till": "April 12, 2022",
        "about": "Responsibilities: sfjnkjnk,jnnns",
        "apply_here": "Apply here",
    },
]


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


if __name__ == "__main__":
    app.run(debug=True)
