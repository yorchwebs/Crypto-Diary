from flask import Flask

from app.emails.emails import mail

from app.db.database import database

from app.index.views import index_bp

from flask_wtf.csrf import CSRFProtect

from datetime import datetime, timedelta

from app.emails.models import Newsletter

from app.emails.emails import send_email

from apscheduler.schedulers.background import BackgroundScheduler

csrf = CSRFProtect()

scheduler = BackgroundScheduler()


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    mail.init_app(app)
    csrf.init_app(app)
    send_email()

    app.register_blueprint(index_bp)

    database.create_tables([Newsletter])

    scheduler.add_job(
        send_email,
        "interval",
        minutes=1,
        next_run_time=datetime.now() + timedelta(seconds=10),
    )
    scheduler.start()

    return app
