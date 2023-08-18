from flask import Flask

from app.db.database import database

from app.index.views import index_bp

from flask_wtf.csrf import CSRFProtect

from datetime import datetime, timedelta

from app.emails.models import Newsletter

from app.emails.emails import SenderEmail

from apscheduler.schedulers.background import BackgroundScheduler

csrf = CSRFProtect()

email = SenderEmail()

send_mail = email.mail

scheduler = BackgroundScheduler()


def create_app(config):
    app = Flask(__name__)

    app.config.from_object(config)

    email.init_app(app)
    csrf.init_app(app)
    email.init_app(app)

    app.register_blueprint(index_bp)

    database.create_tables([Newsletter])

    scheduler.add_job(
        send_mail,
        "interval",
        minutes=1,
        next_run_time=datetime.now() + timedelta(seconds=10),
    )
    scheduler.start()

    return app
