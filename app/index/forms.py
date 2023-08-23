"""
Forms for the index blueprint.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class NewsletterForm(FlaskForm):
    """
    A form for subscribing to a newsletter.

    Attributes:
        name (StringField): A field for the user's name (required, 4-20 characters).
        email (StringField): A field for the user's email (required).
        submit (SubmitField): A button for submitting the form.
    """
    name = StringField("Name", validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Suscribirme")
