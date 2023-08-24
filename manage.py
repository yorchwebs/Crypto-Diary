""" This is the entry point of the application. """

from app import create_app
from config import config

import click
from werkzeug.serving import run_simple
from flask_sijax import Sijax

config_name = config['development']
app = create_app(config_name)
sijax = Sijax(app)

@click.command()
@click.option('--host', '-h', default='127.0.0.1', help='The server host')
@click.option('--port', '-p', default=5000, help='The server port')
def runserver(host, port):
    click.echo('Ejecutando el servidor de desarrollo Flask...')
    sijax.register_flask(app)
    run_simple(host, port, app, use_reloader=True)

app.cli.add_command(runserver)


if __name__ == "__main__":
    app.run()
