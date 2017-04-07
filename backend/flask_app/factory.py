# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for module."""


import os

from flask import Flask
from flask_cors import CORS
from .app_utils import utilities
from .config import CONFIG
from .models import db


def create_app():
    """Configure the app w.r.t Flask-security, databases, loggers."""
    app = Flask(__name__)
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(CONFIG[config_name])
    utilities.setup_logger()
    db.init_app(app)
    CORS(app, headers=['Content-Type'])

    return app



