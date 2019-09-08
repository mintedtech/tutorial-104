from app import app


# If a user tries to access either no page (e.g. www.touro.edu)
# or the index page, then call index()
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
