from app import mail

from datetime import datetime

from flask_mail import Message

from app.index.crypto_prices import CryptoPrice

from concurrent.futures import ThreadPoolExecutor

current_date = datetime.now()

emails = [
    "georgepromotions@gmail.com",
    "georgegarciacode@outlook.com",
    "contacto@jorgegarciadev.com",
]

message = (
    "Los precio de las criptomonedas al día de hoy son:"
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
        f"El precio de {symbol} {name} en USD es de: {usd} y en MXN es de: {mxn} \n"
    )


def send_email():
    try:
        with ThreadPoolExecutor(max_workers=2) as executor:
            for email in emails:
                msg = Message(
                    "Precios de cryptomonedas al día hoy", recipients=[email]
                )
                msg.body = "Contenido del correo"
                executor.submit(mail.send(msg))

            return "Correo enviado"

    except Exception as e:
        return str(e)
