# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for module."""


import os

from flask import Flask
from flask_cors import CORS
from sqlalchemy import text

from .app_utils import utilities
from .config import CONFIG
from .models import db, Ethnicity
from sqlalchemy.orm import sessionmaker

def create_app():
    """Configure the app w.r.t Flask-security, databases, loggers."""
    app = Flask(__name__)
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(CONFIG[config_name])
    utilities.setup_logger()
    db.init_app(app)
    with app.app_context():
        db.create_all()
       # fill_models()
    CORS(app, headers=['Content-Type'])

    return app

def fill_models():
    if not Ethnicity.query.first():
        getCollegesByEthnicity()
    pass


def getCollegesByEthnicity():
    colleges_by_ethnicity = 'SELECT UNITID, INSTNM, UGDS, UGDS_WHITE, UGDS_BLACK, UGDS_HISP, UGDS_ASIAN, UGDS_AIAN, ' \
                          'UGDS_NHPI, UGDS_2MOR, UGDS_NRA, UGDS_UNKN FROM Scorecard'
    sql = text(colleges_by_ethnicity)
    result = db.engine.execute(sql)
    Ethnicities = []
    for row in result:
        Ethnicity(unitID=row[0], College = row[1], UGDS = row[2], UGDS_WHITE = row[3], UGDS_BLACK = row[4], UGDS_HISP=row[5],
                  UGDS_ASIAN=row[6], UGDS_AIAN=row[7], UGDS_NHPI=row[8], UGDS_2MOR=row[9], UGDS_NRA=row[10], UGDS_UNKN=row[11])
        Ethnicities.append(Ethnicity)
    db.session.bulk_save_objects(Ethnicities)
    db.session.commit()


