import smtplib
import logging

from decouple import config
from datetime import datetime
from email.mime.text import MIMEText
from app.index.models import Newsletter
from concurrent.futures import ThreadPoolExecutor
from app.index.crypto_prices import CryptoPrice


class SenderEmail:
    def __init__(self):
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
        smtp_server = config("MAIL_SERVER")
        smtp_port = config("MAIL_PORT")
        smtp_username = config("MAIL_USERNAME")
        smtp_password = config("MAIL_PASSWORD")

        try:
            with ThreadPoolExecutor(max_workers=4) as executor:
                for email in self.emails:
                    message = self.generate_message()
                    msg = MIMEText(message)
                    msg["Subject"] = "Crypto Diary - Newsletter"
                    msg["From"] = smtp_username
                    msg["To"] = email

                    with smtplib.SMTP(smtp_server, smtp_port) as server:
                        server.starttls()
                        server.login(smtp_username, smtp_password)
                        server.sendmail(smtp_username, [email], msg.as_string())

                    executor.submit(logging.info, f"Correo enviado a: {email}")
        except Exception as e:
            logging.error(f"Error en el envío de correos: {str(e)}")
