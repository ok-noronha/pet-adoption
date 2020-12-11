"""Forms for adopt app."""
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPetForm(FlaskForm):
    """ Form to add a pet. """
    name = StringField("Name",
                       validators=[InputRequired()])
    species = StringField("Species",
                          validators=[InputRequired()])
    photo_url = StringField("Photo URL",
                            validators=[Optional(), URL()])
    age = SelectField("Age",
                      choices=[('baby', 'young', 'adult', 'senior'),
                               ('Baby', 'Young', 'Adult', 'Senior')],
                      validators=[InputRequired()])
    notes = StringField("Notes",
                        validators=[Optional()])
