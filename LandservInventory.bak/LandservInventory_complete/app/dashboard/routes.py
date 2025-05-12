from flask import Blueprint, render_template
from flask_login import login_required
from app import db
from app.models import Material, Equipment

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@dashboard_bp.route('/dashboard')
@login_required
def index():
    low_stock = Material.query.filter(Material.quantity <= 10).all()
    overdue_inspections = Equipment.query.filter(Equipment.inspection_due < db.func.current_date()).all()
    overdue_oil = Equipment.query.filter(Equipment.oil_change_due < db.func.current_date()).all()
    return render_template('dashboard.html', low_stock=low_stock,
                           overdue_inspections=overdue_inspections,
                           overdue_oil_changes=overdue_oil)
