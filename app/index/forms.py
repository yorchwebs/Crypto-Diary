""" Forms for the index blueprint. """

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewsletterSubscriberForm(FlaskForm):
    """A form for subscribing to a newsletter.

    Attributes:
        name (StringField): A field for the user's name
                            (required, 4-20 characters).
        submit (SubmitField): A button for submitting the form.
    """

    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Suscribirme")
