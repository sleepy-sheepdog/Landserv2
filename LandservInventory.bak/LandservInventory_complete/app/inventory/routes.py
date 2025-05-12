from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.inventory.forms import MaterialForm
from app import db
from app.models import Material

inventory_bp = Blueprint('inventory', __name__, template_folder='templates/inventory')

@inventory_bp.route('/materials')
@login_required
def list_materials():
    mats = Material.query.all()
    return render_template('materials.html', materials=mats)

@inventory_bp.route('/materials/add', methods=['GET','POST'])
@login_required
def add_material():
    form = MaterialForm()
    if form.validate_on_submit():
        m = Material(
            name=form.name.data,
            quantity=form.quantity.data,
            unit=form.unit.data,
            unit_price=form.unit_price.data,
            supplier=form.supplier.data,
            material_type=form.material_type.data,
            description=form.description.data,
            owner=current_user
        )
        db.session.add(m)
        db.session.commit()
        flash('Material added', 'success')
        return redirect(url_for('inventory.list_materials'))
    return render_template('add_material.html', form=form)

@inventory_bp.route('/materials/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit_material(id):
    m = Material.query.get_or_404(id)
    form = MaterialForm(obj=m)
    if form.validate_on_submit():
        form.populate_obj(m)
        db.session.commit()
        flash('Material updated', 'success')
        return redirect(url_for('inventory.list_materials'))
    return render_template('add_material.html', form=form)

@inventory_bp.route('/materials/delete/<int:id>', methods=['POST'])
@login_required
def delete_material(id):
    m = Material.query.get_or_404(id)
    db.session.delete(m)
    db.session.commit()
    flash('Material deleted', 'success')
    return redirect(url_for('inventory.list_materials'))
