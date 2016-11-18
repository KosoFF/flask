from flask_wtf import FlaskForm
from wtforms import StringField,  BooleanField, PasswordField
from wtforms.validators import Required


class LoginForm(FlaskForm):
    email = StringField('Email adress', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)


