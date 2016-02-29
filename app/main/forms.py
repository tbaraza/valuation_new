from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,Length,Regexp,Required


class LoginForm(Form):
    # openid = StringField('openid', validators=[DataRequired()])
    # remember_me = BooleanField('remember_me', default=False)
    email = StringField('Email',validators=[Required(),Email()])
    password= PasswordField('Password',validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')



class ValuesForm(Form):
    sales_amount = IntegerField('Sales', validators=[DataRequired()])
    cost = IntegerField('Cost of goods sold', validators=[DataRequired()])
    expenses = IntegerField('Expenses', validators=[DataRequired()])
    tax = IntegerField('Tax', validators=[DataRequired()])
    submit = SubmitField('Submit')
