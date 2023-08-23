""" Views for the index blueprint. """

from flask import flash
from flask import url_for
from flask import redirect
from flask import Blueprint
from flask import render_template

from app.index.models import Newsletter

from app.index.forms import NewsletterForm

from app.index.crypto_prices import CryptoPrice

from concurrent.futures import ThreadPoolExecutor

from app.index.utils.pydantic_validator import NewsletterModel


index_bp = Blueprint(
    "index_bp", __name__, template_folder="templates", static_folder="static"
)


@index_bp.route("/", methods=["GET", "POST"])
def index():
    """
    Renders the index page and handles the newsletter subscription form.

    Returns:
        A rendered HTML template with the index page and the crypto prices.
    """
    form = NewsletterForm()
    if form.validate_on_submit():
        validate_data = NewsletterModel(name=form.name.data, email=form.email.data)
        try:
            with ThreadPoolExecutor(max_workers=4) as executor:
                new_subscriber = Newsletter.create(
                    name=validate_data.name, email=validate_data.email
                )
                executor.submit(new_subscriber.save())
                flash("Gracias por suscribirte !!")
            return redirect(url_for("index_bp.index"))

        except Exception:
            flash("El email ya existe en la base de datos")
            return redirect(url_for("index_bp.index"))

    crypto_prices = CryptoPrice().prices

    return render_template(
        "index.html",
        form=form,
        **crypto_prices,
    )
