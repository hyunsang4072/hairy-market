from flask import Flask, render_template
# from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy

# create an instance of Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

from market import routes