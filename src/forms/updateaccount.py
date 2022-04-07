from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    resume = FileField('Update CV', validators=[FileAllowed(['pdf'])])
    submit = SubmitField('Update')
