from flask_mail import Mail
from flask_mail import Message

from datetime import datetime
from app.emails.models import Newsletter

from app.index.crypto_prices import CryptoPrice

from concurrent.futures import ThreadPoolExecutor

mail = Mail()

current_date = datetime.now()

emails = [email.email for email in Newsletter.select()]

message = (
    "Éstos son los precio de las criptomonedas al día de hoy - "
    + current_date.strftime("%d/%m/%Y")
    + " \n\n"
)

for symbol, name, usd, mxn in zip(
    CryptoPrice().prices["symbol_list"],
    CryptoPrice().prices["name_list"],
    CryptoPrice().prices["usd_price_list"],
    CryptoPrice().prices["mxn_price_list"],
):
    message += (
        f"El precio de {symbol} - {name} en USD es de: ${usd} y en MXN es de: ${mxn} \n"
    )


def send_email():
    try:
        with ThreadPoolExecutor(max_workers=2) as executor:
            for email in emails:
                msg = Message("Crypto Diary - Newsletter", recipients=[email])
                msg.body = message
                executor.submit(mail.send(msg))

    except Exception as e:
        return str(e)
