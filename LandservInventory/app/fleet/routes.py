import os
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from app.fleet.forms import EquipmentForm, ServiceLogForm
from app import db
from app.models import Equipment, ServiceLog
from werkzeug.utils import secure_filename

fleet_bp = Blueprint('fleet', __name__, template_folder='templates/fleet')
UPLOAD_FOLDER = 'static/uploads'

@fleet_bp.route('/equipment')
@login_required
def equipment():
    items = Equipment.query.all()
    return render_template('equipment.html', equipment=items)

@fleet_bp.route('/equipment/add', methods=['GET','POST'])
@login_required
def add_equipment():
    form = EquipmentForm()
    if form.validate_on_submit():
        image_path = None
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            path = os.path.join(current_app.root_path, UPLOAD_FOLDER, filename)
            form.image.data.save(path)
            image_path = filename
        eq = Equipment(
            name=form.name.data,
            type=form.type.data,
            make=form.make.data,
            model=form.model.data,
            year=form.year.data,
            mileage=form.mileage.data,
            inspection_due=form.inspection_due.data,
            oil_change_due=form.oil_change_due.data,
            notes=form.notes.data,
            image_path=image_path,
            added_by=current_user.id
        )
        db.session.add(eq)
        db.session.commit()
        flash('Equipment added', 'success')
        return redirect(url_for('fleet.equipment'))
    return render_template('add_equipment.html', form=form)

@fleet_bp.route('/service_logs')
@login_required
def list_service_logs():
    logs = ServiceLog.query.all()
    return render_template('service_logs.html', service_logs=logs)

@fleet_bp.route('/service_logs/add', methods=['GET','POST'])
@login_required
def add_service_log():
    form = ServiceLogForm()
    if form.validate_on_submit():
        photo_path = None
        if form.photo.data:
            filename = secure_filename(form.photo.data.filename)
            path = os.path.join(current_app.root_path, UPLOAD_FOLDER, filename)
            form.photo.data.save(path)
            photo_path = filename
        log = ServiceLog(
            equipment_id=request.args.get('eq_id'),
            service_date=form.service_date.data,
            description=form.description.data,
            photo_path=photo_path,
            added_by=current_user.id
        )
        db.session.add(log)
        db.session.commit()
        flash('Service log added', 'success')
        return redirect(url_for('fleet.list_service_logs'))
    return render_template('add_service_log.html', form=form)
