import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from dotenv import load_dotenv

load_dotenv()
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.auth.routes import auth_bp
    from app.inventory.routes import inventory_bp
    from app.fleet.routes import fleet_bp
    from app.admin.routes import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(inventory_bp, url_prefix='/inventory')
    app.register_blueprint(fleet_bp, url_prefix='/fleet')
    app.register_blueprint(admin_bp, url_prefix='/admin')

    from app.dashboard.routes import dashboard_bp
    app.register_blueprint(dashboard_bp)

    return app
