"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL, AnyOf


class AddPetForm(FlaskForm):
    """ Form to add a pet. """
    name = StringField("Name",
                       validators=[InputRequired()])
    species = StringField("Species",
                          validators=[InputRequired(),
                                      AnyOf(['porcupine', 'cat', 'dog'], "Must be cat, dog, or porcupine.")])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    age = SelectField("Age",
                      choices=[('baby', 'Baby'),
                               ('young', 'Young'),
                               ('adult', 'Adult'),
                               ('senior', 'Senior')])
    notes = StringField("Notes",
                        validators=[Optional()])


class EditPetForm(FlaskForm):
    """ Form to edit a pet. """
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    notes = StringField("Notes",
                        validators=[Optional()])
    available = BooleanField("Available")
