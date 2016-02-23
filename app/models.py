from app import db


class DataModel(db.Model):
    __tablename__ = 'data'
    uid = db.Column(db.Integer, primary_key=True)
    sales_amount = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    expenses = db.Column(db.Integer)
    tax = db.Column(db.Integer)

    def __init__(self, sales_amount, cost, expenses, tax):
        self.sales_amount = sales_amount
        self.cost = cost
        self.expenses = expenses
        self.tax = tax
