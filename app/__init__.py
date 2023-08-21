from flask import Flask

from app.db.database import database

from app.index.views import index_bp

from emails.emails import SenderEmail

from flask_wtf.csrf import CSRFProtect

from app.index.models import Newsletter

from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

csrf = CSRFProtect()

scheduler = BackgroundScheduler()


def send_emails_job():
    email_sender = SenderEmail()
    email_sender.send_email()


def create_app(config):
    app.config.from_object(config)

    csrf.init_app(app)

    app.register_blueprint(index_bp)

    database.create_tables([Newsletter])

    send_time = datetime.now() + timedelta(seconds=10)
    scheduler.add_job(
        send_emails_job,
        "interval",
        days=1,
        start_date=send_time,
        id="send_emails_job",
    )
    scheduler.start()

    return app
