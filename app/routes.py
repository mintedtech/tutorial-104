# Use rendered templates: HTML pages combined with Python data
from flask import render_template
# As done before, import the app variable from the app package
from app import app


# If a user tries to access either no page (e.g. www.touro.edu)
# nor the index page, then call index()
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
