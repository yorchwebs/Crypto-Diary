from flask import Flask

from app.index.models import Newsletter

from app.db.database import database

from app.index.views import index_bp

# Iniciamos la Aplicación.
app = Flask(__name__)

app.register_blueprint(index_bp)

def create_app(config):
    app.config.from_object(config)
    # csrf.init_app(app)
    # app.register_error_handler(404, page_not_found)
    database.drop_tables([Newsletter])
    database.create_tables([Newsletter])
    return app