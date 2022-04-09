from flask_wtf import FlaskForm
from wtforms import Form, StringField,SubmitField
class SearchForm(Form):
    search = StringField("Search")
    submit = SubmitField('Search')
