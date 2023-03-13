from flask_wtf import FlaskForm
from wtforms import StringField, FileField, SubmitField, SelectField, IntegerField, TextAreaField, DecimalField
from wtforms.validators import InputRequired, EqualTo, Email
from flask_wtf.file import FileAllowed, DataRequired


class AddPropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()], render_kw={"rows": 5})
    rooms = IntegerField('No. of Rooms', validators=[DataRequired()])
    bathrooms = DecimalField('No. of Bathrooms', validators=[DataRequired()], places=1)
    price = DecimalField('Price', validators=[DataRequired()], places=2)
    property_type = SelectField('Property Type', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    main_photo = FileField('Photo', validators=[DataRequired(), FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'bmp'], 'Only imnages are allowed to be sent')])
    submit = SubmitField('Add Property')