from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.Enum('admin','crew_leader','crew_member'), nullable=False)
    materials = db.relationship('Material', backref='owner', lazy=True)
    equipment = db.relationship('Equipment', backref='owner', lazy=True)

class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    unit = db.Column(db.String(20))
    unit_price = db.Column(db.Float)
    supplier = db.Column(db.String(120))
    material_type = db.Column(db.String(50))
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    type = db.Column(db.String(50))
    make = db.Column(db.String(80))
    model = db.Column(db.String(80))
    year = db.Column(db.Integer)
    mileage = db.Column(db.Integer)
    inspection_due = db.Column(db.Date)
    oil_change_due = db.Column(db.Date)
    notes = db.Column(db.Text)
    image_path = db.Column(db.String(200))
    added_by = db.Column(db.Integer, db.ForeignKey('user.id'))
    service_logs = db.relationship('ServiceLog', backref='equipment', lazy=True)

class ServiceLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'), nullable=False)
    service_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text)
    photo_path = db.Column(db.String(200))
    added_by = db.Column(db.Integer, db.ForeignKey('user.id'))
