from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Optional

class MaterialForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    quantity = IntegerField('Quantity', validators=[InputRequired()])
    unit = StringField('Unit', validators=[InputRequired()])
    unit_price = FloatField('Unit Price', validators=[InputRequired()])
    supplier = StringField('Supplier', validators=[InputRequired()])
    material_type = StringField('Type', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    submit = SubmitField('Save')
