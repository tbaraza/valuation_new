from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)


class ValuesForm(Form):
    sales_amount = IntegerField('Sales', validators=[DataRequired()])
    cost = IntegerField('Cost of goods sold', validators=[DataRequired()])
    expenses = IntegerField('Expenses', validators=[DataRequired()])
    tax = IntegerField('Tax', validators=[DataRequired()])
    submit = SubmitField('Submit')
