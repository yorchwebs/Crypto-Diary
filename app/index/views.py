from flask import Blueprint, render_template

from app.index.crypto_prices import CryptoPrices

index_bp = Blueprint(
    "index_bp", __name__, template_folder="templates", static_folder="static"
)


# Ruta y función para obtener datos.
@index_bp.route("/")
def index():
        return render_template(
            "index.html",
            coins_list=CryptoPrices().get_prices()["coins_list"],
            name_list = CryptoPrices().get_prices()["name_list"],
            usd_price_list=CryptoPrices().get_prices()["usd_price_list"],
            mxn_price_list=CryptoPrices().get_prices()["mxn_price_list"],
        )
