from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField

class UserRoleForm(FlaskForm):
    role = SelectField('Role', choices=[('admin','Admin'),('crew_leader','Crew Leader'),('crew_member','Crew Member')])
    submit = SubmitField('Update')
