# Use rendered templates: HTML pages combined with Python data
from flask import render_template, flash, redirect, url_for
# As done before, import the app variable from the app package
from app import app
# import the LoginForm class from forms.py in our app package
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


# If a user tries to access either no page (e.g. www.touro.edu)
# or the index page, then call index()
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'SA'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Robin'},
            'body': 'The vacation we took was so nice!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)