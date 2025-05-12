from flask import Blueprint, render_template, abort, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import User
from app.admin.forms import UserRoleForm

admin_bp = Blueprint('admin', __name__, template_folder='templates/admin')

@admin_bp.route('/dashboard', methods=['GET','POST'])
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        abort(403)
    users = User.query.all()
    user_forms = {}
    for u in users:
        form = UserRoleForm(prefix=str(u.id))
        form.role.data = u.role
        user_forms[u.id] = form
    for uid, form in user_forms.items():
        if form.validate_on_submit() and form.submit.data:
            new_role = form.role.data
            user = User.query.get(uid)
            user.role = new_role
            db.session.commit()
            flash(f"Updated {user.username}'s role to {new_role}.", 'success')
            return redirect(url_for('admin.admin_dashboard'))
    return render_template('admin_dashboard.html', users=users, user_forms=user_forms)
