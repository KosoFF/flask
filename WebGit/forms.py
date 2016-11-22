from flask_wtf import FlaskForm
from wtforms import StringField,  BooleanField, PasswordField, SubmitField
from wtforms import validators


class LoginForm(FlaskForm):
    email = StringField('Email adress', [validators.InputRequired()])
    password = PasswordField('Password', [validators.InputRequired()])
    remember_me = BooleanField('remember_me', default=False)
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField('Register')


class RepositoryAddForm(FlaskForm):
    url = StringField('Repository url', [validators.required(), validators.length(max=120)], id='input_url')
    comment = StringField('Any comments', [validators.optional(), validators.length(max=255)], id='input_comment')
    submit = SubmitField('Add')

    # def validate_email(self, field):
    #     if User.query.filter_by(email=field.data).first():
    #         raise ValidationError('Email already registered')
    #
    # def validate_username(self, field):
    #     if User.query.filter_by(username=field.data).first():
    #         raise ValidationError('Username already exists')