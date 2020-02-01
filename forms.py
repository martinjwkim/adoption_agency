from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, IntegerField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("Dog", "Dog"), ("Cat", "Cat"), ("Porcupine", "Porcupine")])
    image_url = StringField("Image URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[InputRequired(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[("Dog", "Dog"), ("Cat", "Cat"), ("Porcupine", "Porcupine")])
    image_url = StringField("Image URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[InputRequired(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")
    available = SelectField("Availability", choices=[('Available', "Available"), ('Not Available', "Not Available")])
