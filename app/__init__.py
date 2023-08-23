from flask import Flask

from app.index.views import index_bp

from emails.emails import SenderEmail

from flask_wtf.csrf import CSRFProtect

from app.index.models import Newsletter

from datetime import datetime, timedelta

from app.db.database import MySQLDatabaseSingleton

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

csrf = CSRFProtect()

scheduler = BackgroundScheduler()

database = MySQLDatabaseSingleton().database


def send_emails_job():
    """
    A function that sends emails to all subscribers in the database.

    Returns:
        None
    """
    email_sender = SenderEmail()
    email_sender.send_emails()


def create_app(config):
    """
    Creates and configures the Flask application.

    Args:
        config (str): The name of the configuration class to use for the Flask
        application.

    Returns:
        The configured Flask application instance.
    """
    app.config.from_object(config)

    csrf.init_app(app)

    app.register_blueprint(index_bp)

    with app.app_context():
        database.create_tables([Newsletter], safe=True)

    send_time = datetime.now() + timedelta(seconds=10)
    scheduler.add_job(
        send_emails_job,
        "interval",
        minutes=1,
        start_date=send_time,
        id="send_emails_job",
    )
    scheduler.start()

    return app
