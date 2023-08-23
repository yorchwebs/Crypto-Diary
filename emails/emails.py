""" This is a docstring for the `SenderEmail`. """

import smtplib

import logging

from decouple import config

from datetime import datetime

from email.mime.text import MIMEText

from app.index.models import Newsletter

from app.index.crypto_prices import CryptoPrice

from concurrent.futures import ThreadPoolExecutor


class SenderEmail:
    """
    A class that sends a newsletter email with the current prices of popular
    cryptocurrencies.

    This class retrieves the email addresses of the newsletter subscribers
    from a database, and uses the `CryptoPrice` class to get the current prices of
    popular cryptocurrencies in USD and MXN. It generates a message with the
    current date and the prices of each cryptocurrency, and sends it to each subscriber
    using the SMTP server and credentials specified in the configuration file.

    Attributes
    ----------
    current_date : datetime
        The current date and time.
    names : list
        A list of the names of the newsletter subscribers.
    emails : list
        A list of the email addresses of the newsletter subscribers.
    crypto_price : CryptoPrice
        An instance of the `CryptoPrice` class used to retrieve the current prices of
        popular cryptocurrencies.

    Methods
    -------
    generate_message() -> str:
        Generates a message with the current date and the prices of cryptocurrencies
        in USD and MXN.
    email_body_and_connection(email: str) -> None:
        Sends an email to the specified email address using the SMTP server and
        credentials specified in the configuration file.
    send_emails() -> None:
        Sends emails to all recipients in the `emails` list using a thread pool.
    """

    def __init__(self) -> None:
        """
        Initializes a `SenderEmail` instance.

        This method initializes the `current_date` attribute with the current
        date and time, retrieves the names and email addresses of the newsletter
        subscribers from the database using the `Newsletter` model, and initializes an
        instance of the `CryptoPrice` class to retrieve the current prices of popular
        cryptocurrencies.

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.current_date = datetime.now()
        self.names = [name.name for name in Newsletter.select()]
        self.emails = [email.email for email in Newsletter.select()]
        self.crypto_price = CryptoPrice()

    def generate_message(self) -> str:
        """
        Generates a message with the current date and the prices of
        cryptocurrencies in USD and MXN.

        This method uses the `CryptoPrice` class to get the current prices of
        cryptocurrencies in USD and MXN. It then generates a message with the
        current date and the prices of each cryptocurrency, formatted as follows:
        "El precio de {symbol} - {coin_name} en USD es: ${usd} y en MXN es: ${mxn}"

        :args:
            None

        :return:
            str = A string with the generated message.

        :examples:
            >>> sender_email = SenderEmail()
            >>> sender_email.generate_message()
            Éstos son los precio de las criptomonedas al día de hoy - 01/01/2021
        """
        message = (
            "Éstos son los precio de las criptomonedas al día de hoy - "
            + self.current_date.strftime("%d/%m/%Y")
            + " \n\n"
        )

        for symbol, coin_name, usd, mxn in zip(
            self.crypto_price.prices["symbol_list"],
            self.crypto_price.prices["name_list"],
            self.crypto_price.prices["usd_price_list"],
            self.crypto_price.prices["mxn_price_list"],
        ):
            message += f"El precio de {symbol} - {coin_name} en USD es: ${usd} y en MXN es: ${mxn} \n"

        return message

    def email_body_and_connection(self, email: str) -> None:
        """
        Sends an email to the specified email address using the SMTP server
        and credentials specified in the configuration file.

        Args:
            email: A string representing the email address to send the email to.

        Returns:
            None.

        Raises:
            Any exceptions raised by the smtplib module during the email
            sending process.
        """

        smtp_server: str = config("MAIL_SERVER")
        smtp_port: int = config("MAIL_PORT")
        smtp_username: str = config("MAIL_USERNAME")
        smtp_password: str = config("MAIL_PASSWORD")

        try:
            message = self.generate_message()
            msg = MIMEText(message)
            msg["Subject"] = "Crypto Diary - Newsletter"
            msg["From"] = smtp_username
            msg["To"] = email

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(smtp_username, smtp_password)
                server.sendmail(smtp_username, [email], msg.as_string())

            logging.info(f"Correo enviado a: {email}")
        except Exception as e:
            logging.error(f"Error en el envío de correos: {str(e)}")

    def send_emails(self) -> None:
        """
        Sends emails to all recipients in the `emails` list using a thread pool.

        This method uses a `ThreadPoolExecutor` to send emails concurrently,
        with a maximum of 4 worker threads.
        Each email is sent by calling the `email_body_and_connection` method with the
        corresponding email object as argument.

        :args: None

        :return: None
        """
        with ThreadPoolExecutor(max_workers=4) as executor:
            for email in self.emails:
                executor.submit(self.email_body_and_connection, email)
