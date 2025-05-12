import os
basedir = os.path.abspath(os.path.dirname(__file__))

class DevelopmentConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
