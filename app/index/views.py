"""Views for the index blueprint."""

from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Type

from flask import Blueprint, Response, flash, redirect, render_template, url_for
from flask_wtf.csrf import generate_csrf

from app.index.crypto_prices import CryptoPrice
from app.index.forms import NewsletterSubscriberForm
from app.index.models import NewsletterSubscriber
from app.index.utils.pydantic_validator import (
    NewsletterSubscriberValidateDataModel,  # noqa
)

index_bp = Blueprint(
    "index_bp", __name__, template_folder="templates", static_folder="static"
)


@index_bp.route("/", methods=["GET", "POST"])
def index() -> Response:
    """Renders the index page and handles the newsletter subscription form.

    Returns:
        A rendered HTML template with the index page and the crypto prices.
    """
    form: Type[NewsletterSubscriberForm] = NewsletterSubscriberForm()
    if form.validate_on_submit():
        validate_data: Type[NewsletterSubscriberValidateDataModel] = (
            NewsletterSubscriberValidateDataModel(email=form.email.data)
        )
        try:
            with ThreadPoolExecutor(max_workers=4) as executor:
                new_subscriber: Type[NewsletterSubscriber] = (
                    NewsletterSubscriber.create(email=validate_data.email)
                )
                executor.submit(new_subscriber.save())
                flash(
                    (
                        "success",
                        "¡ Se ha registrado tu correo de forma exitosa !",
                    )
                )  # noqa
            return redirect(url_for("index_bp.index"))

        except Exception:
            flash(
                (
                    "error",
                    "El email ya existe en la base de datos, vuelve a intentarlo...",  # noqa
                )
            )
            return redirect(url_for("index_bp.index"))

    crypto_prices: List[Dict[str, str]] = CryptoPrice().prices
    csrf_token: Type[str] = generate_csrf()

    return render_template(
        "index.html",
        form=form,
        **crypto_prices,
        csrf_token=csrf_token,
    )
