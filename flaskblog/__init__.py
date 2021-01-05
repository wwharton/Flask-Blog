from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = '78dd78dad6a396a8175e8a508ec52100'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login' #this view is my login function in routes
login_manager.login_message_category = 'info' #info is a bootstrap class

# routes import must follow db init otherwise we fall into an import loop
from flaskblog import routes