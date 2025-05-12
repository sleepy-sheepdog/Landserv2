from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, TextAreaField, FileField, SubmitField
from wtforms.validators import InputRequired, Optional

class EquipmentForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    type = StringField('Type', validators=[InputRequired()])
    make = StringField('Make', validators=[Optional()])
    model = StringField('Model', validators=[Optional()])
    year = IntegerField('Year', validators=[Optional()])
    mileage = IntegerField('Mileage', validators=[Optional()])
    inspection_due = DateField('Inspection Due', validators=[Optional()])
    oil_change_due = DateField('Oil Change Due', validators=[Optional()])
    notes = TextAreaField('Notes', validators=[Optional()])
    image = FileField('Image', validators=[Optional()])
    submit = SubmitField('Save')

class ServiceLogForm(FlaskForm):
    service_date = DateField('Date', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    photo = FileField('Photo', validators=[Optional()])
    submit = SubmitField('Save')
