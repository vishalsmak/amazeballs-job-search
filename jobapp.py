from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app= Flask(__name__)

app.config['SECRET_KEY'] = '53070fbaabd54efe45ed035a467ecc3f'

jobs = [
    {
        'company': 'MICROSOFT',
        'job_title': 'GRADUATE SOFTWARE ENGINEER',
        'location': 'London',
        'date_posted': 'January 10, 2022',
        'apply_till': 'March 30, 2022',
        'about': 'Responsibilities: sfjnkjnk,jn',
        'apply_here': 'apply here',
    },
    {
        'company': 'DEUTSCH BANK',
        'job_title': 'GRADUATE SOFTWARE ENGINEER',
        'location': 'London',
        'date_posted': 'January 10, 2022',
        'apply_till': 'March 30, 2022',
        'about': 'Responsibilities: sfjnkjnk,jn',
        'apply_here': 'apply here',
    }
]

@app.route("/")
@app.route("/home")
def welcome():
    return render_template('home.html', jobs= jobs)

@app.route("/register")
def register():
    form= RegistrationForm()
    return render_template('register.html',title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
