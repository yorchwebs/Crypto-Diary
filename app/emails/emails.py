from flask_mail import Mail
from flask_mail import Message

from datetime import datetime
from app.emails.models import Newsletter

from app.index.crypto_prices import CryptoPrice

from concurrent.futures import ThreadPoolExecutor


class SenderEmail:
    def __init__(self):
        self.mail = Mail()
        self.current_date = datetime.now()
        self.emails = [email.email for email in Newsletter.select()]
        self.crypto_price = CryptoPrice()

    def generate_message(self):
        message = (
            "Éstos son los precio de las criptomonedas al día de hoy - "
            + self.current_date.strftime("%d/%m/%Y")
            + " \n\n"
        )

        for symbol, name, usd, mxn in zip(
            self.crypto_price.prices["symbol_list"],
            self.crypto_price.prices["name_list"],
            self.crypto_price.prices["usd_price_list"],
            self.crypto_price.prices["mxn_price_list"],
        ):
            message += f"El precio de {symbol} - {name} en USD es de: ${usd} y en MXN es de: ${mxn} \n"

        return message

    def send_email(self):
        try:
            with ThreadPoolExecutor(max_workers=2) as executor:
                for email in self.emails:
                    msg = Message("Crypto Diary - Newsletter", recipients=[email])
                    msg.body = self.generate_message()
                    executor.submit(self.mail.send(msg))

        except Exception as e:
            return str(e)
