import os

class Config:

    # Generate New Key, Set up with Environ Variables on deploy
    SECRET_KEY = '78dd78dad6a396a8175e8a508ec52100'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    # Flask Mail config, including windows environment variables
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True

    # OS Environment Variables need to be set on the deployed machine
    # For use in venv, hardcode or activate the values
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')