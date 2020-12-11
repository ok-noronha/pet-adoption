"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DFLT_IMG = ''


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """ pet class """

    __tabtlename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                        nullable=False)
    photo_url = db.Column(db.Text,
                          nullable=False,
                          server_default=DFLT_IMG)
    age = db.Column(db.Text,
                    nullable=False)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                          nullable=False,
                          server_default=True)


