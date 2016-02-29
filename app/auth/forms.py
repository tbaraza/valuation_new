from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email, Length, Regexp, Required, EqualTo
from ..models import User


class LoginForm(Form):

    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class ValuesForm(Form):
    sales_amount = IntegerField('Sales', validators=[DataRequired()])
    cost = IntegerField('Cost of goods sold', validators=[DataRequired()])
    expenses = IntegerField('Expenses', validators=[DataRequired()])
    tax = IntegerField('Tax', validators=[DataRequired()])
    submit = SubmitField('Submit')


class RegistrationForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        Required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                          'Usernames must have only letters, '
                                          'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        Required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')