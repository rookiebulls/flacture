# -*- coding: utf-8 -*-
"""
    flacture.config
    ~~~~~~~~~~~~~~~

    flacture cofigurations
"""

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(24))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(basedir, '..', 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_USE_ENCODE_METHODS = True


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
