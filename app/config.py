import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Examples
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/conversion_db'
    # Other examples
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False