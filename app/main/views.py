from flask import render_template
from . import main
from flask import render_template, redirect, request, url_for, flash, g
from forms import ValuesForm
from flask.ext.login import login_required

# index view function suppressed for brevity

@main.route('/', methods=['GET', 'POST'])
def index():
    posts = [
        {
            'author': {'nickname': 'John'},
            'sales_amount': 5000,
            'cost': 200,
            'expenses': 300,
            'tax': 400
        },
        {
            'author': {'nickname': 'Susan'},
            'id': 2,
            'sales_amount': 50000,
            'cost': 2000,
            'expenses': 3000,
            'tax': 4000

        }]
    form = ValuesForm()

    if request.method == 'GET':
        return render_template('index.html', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            # flash('All fields are required="%s"' % (form.sales_amount.data))
            for field, errors in form.errors.items():
                flash(u"Error in the %s field - %s" %
                      (getattr(form, field).label.text, errors))

            if form.sales_amount.data and form.cost.data and form.expenses.data and form.tax.data:
                profit = form.sales_amount.data - form.cost.data - \
                    form.expenses.data - form.tax.data
                flash('Your profit is: %d' % profit)
                return redirect(url_for('main.index'))

        return render_template('index.html', posts=posts, form=form)



"""
@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
    return render_template('login.html',
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('values'))


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember=remember_me)
    return redirect(request.args.get('next') or url_for('values'))



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('values'))


@app.route('/user/<nickname>')
@login_required
def user(nickname):
    user = User.query.filter_by(nickname=nickname).first()
    if user == None:
        flash('User %s not found.' % nickname)
        return redirect(url_for('index'))
    posts = [
        {'author': user, 'sales_amount': 3000,
            'cost': 200, 'expenses': 100, 'tax': 50},
        {'author': user, 'sales_amount': 4000,
            'cost': 200, 'expenses': 100, 'tax': 50}
    ]
    return render_template('user.html',
                           user=user,
                           posts=posts)

    """
