from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


class NewsletterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Suscribirme")
