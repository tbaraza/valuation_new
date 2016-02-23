
from flask import render_template, flash, redirect, request, url_for
from app import app
from .forms import LoginForm
from .forms import ValuesForm

# index view function suppressed for brevity


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenId="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('values')
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])


@app.route('/values', methods=['GET', 'POST'])
def values():
    form = ValuesForm()

    if request.method == 'GET':
        return render_template('values.html', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            # flash('All fields are required="%s"' % (form.sales_amount.data))
            for field, errors in form.errors.items():
                flash(u"Error in the %s field - %s" %
                      (getattr(form, field).label.text, error))

            if form.sales_amount.data and form.cost.data and form.expenses.data and form.tax.data:
                profit = form.sales_amount.data - form.cost.data - \
                    form.expenses.data - form.tax.data
                flash('Your profit is: %d' % profit)
                return redirect(url_for('values'))

        return render_template('values.html', form=form)
