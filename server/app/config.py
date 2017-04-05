"""This module has configurations for flask app."""

import logging
import os

CONFIG = {
    "development": "app.config.DevelopmentConfig",
    "testing": "app.config.TestingConfig",
    "production": "app.config.ProductionConfig",
    "default": "app.config.ProductionConfig"
}


class BaseConfig(object):
    """Base class for default set of configs."""

    DEBUG = False
    TESTING = False
    LOGGING_FORMAT = "[%(asctime)s] [%(funcName)-30s] +\
                                    [%(levelname)-6s] %(message)s"
    LOGGING_LOCATION = 'web.log'
    LOGGING_LEVEL = logging.DEBUG
    CACHE_TYPE = 'simple'
    COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml',
                          'application/json', 'application/javascript']
    WTF_CSRF_ENABLED = False
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500


class DevelopmentConfig(BaseConfig):
    """Default set of configurations for development mode."""

    DEBUG = True
    TESTING = False
    BASEDIR = os.path.abspath(os.path.dirname(__file__))


class ProductionConfig(BaseConfig):
    """Default set of configurations for prod mode."""

    DEBUG = False
    TESTING = False
    BASEDIR = os.path.abspath(os.path.dirname(__file__))


class TestingConfig(BaseConfig):
    """Default set of configurations for test mode."""

    DEBUG = False
    TESTING = True
