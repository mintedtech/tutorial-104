from flask import Flask
# Import the Config class from the config.py file
from config import Config
# Database
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


# This statement sets the app variable, which sets the app's name to main
# when this file is started using the run button or command line run
app = Flask(__name__, template_folder='../templates')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# This import must come AFTER the statement: app = Flask (__name__)
# The reason for this is that routes.py, referenced below,
# refers to the app variable above. So, the import must be after this app=
# That's why this import isn’t at the top, unlike PyCharm's recommendation
# This tells Python to check the routes file in this app package
# This file determines what function each HTML page should run
from app import routes, models
