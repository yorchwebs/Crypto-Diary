from flask import Flask

from flask_mail import Mail

from datetime import datetime

from app.db.database import database

from app.index.views import index_bp

from flask_wtf.csrf import CSRFProtect

from app.emails.emails import send_email

from app.emails.models import Newsletter

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

mail = Mail(app)

app.register_blueprint(index_bp)

csrf = CSRFProtect()

scheduler = BackgroundScheduler()


def create_app(config):
    try:
        csrf.init_app(app)
        app.config.from_object(config)
        database.create_tables([Newsletter])
        scheduler.add_job(
            send_email, "interval", minutes=1, next_run_time=datetime.now()
        )
        scheduler.start()

        return app

    except Exception as e:
        return str(e)
