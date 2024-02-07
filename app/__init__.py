from flask import Flask

from datetime import datetime

from emails.emails import SenderEmail

from flask_wtf.csrf import CSRFProtect

from app.index.views import index_bp
from app.index.models import NewsletterSubscriber
from app.db.database import MySQLDatabaseSingleton

from apscheduler.triggers.cron import CronTrigger
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

csrf = CSRFProtect()

scheduler = BackgroundScheduler()

database = MySQLDatabaseSingleton().database


def send_emails_job():
    """A function that sends emails to all subscribers in the database.

    Returns:
        None
    """
    email_sender = SenderEmail()
    email_sender.send_emails()


def create_app(config):
    """Creates and configures the Flask application.

    Args:
        config (str): The name of the configuration class to use for the Flask
        application.

    Returns:
        The configured Flask application instance.
    """

    time_of_send_email = "08:00"

    app.config.from_object(config)

    csrf.init_app(app)

    app.register_blueprint(index_bp)

    with app.app_context():
        database.create_tables([NewsletterSubscriber], safe=True)

    send_time = datetime.now()
    scheduler.add_job(
        send_emails_job,
        CronTrigger(
            hour=time_of_send_email.split(":")[0],
            minute=time_of_send_email.split(":")[1],
        ),
        id="send_emails_job",
        next_run_time=send_time,
    )
    scheduler.start()

    return app
