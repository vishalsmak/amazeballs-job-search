from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms.widgets import TextArea

class ApplicationForm(FlaskForm):
    phone = StringField('Phone number',
                           validators=[DataRequired()])
    name = StringField('Name',validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    github = StringField('Github account',validators=[DataRequired()])
    cover = StringField(u'Cover Letter', widget=TextArea())
    resume = FileField('Add your CV', validators=[FileAllowed(['pdf'])])
    submit = SubmitField('Submit')
