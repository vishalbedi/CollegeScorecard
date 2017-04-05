
"""Entry point for the server application."""

import logging
import traceback
import os
from flask import Flask
from flask_cors import CORS
from gevent.wsgi import WSGIServer
from .config import CONFIG
from .app_utils import utilities

logger = logging.getLogger(__name__)


def create_app():
    """Configure the app w.r.t Flask-security, databases, loggers."""
    app = Flask(__name__)
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(CONFIG[config_name])
    utilities.setup_logger()
    CORS(app, headers=['Content-Type'])
    return app

# main application instance
main_app = create_app()


def main():
    """Main entry point of the app."""
    try:
        http_server = WSGIServer(('0.0.0.0', 8080),
                                 main_app,
                                 log=logging,
                                 error_log=logging)

        http_server.serve_forever()
    except Exception as exc:
        logger.error(exc.message)
        logger.exception(traceback.format_exc())
    finally:
        # get last entry and insert build appended if not completed
        # Do something here
        pass