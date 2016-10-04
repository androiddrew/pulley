# -*- coding: utf-8 -*-
"""
    pulley.config
    ~~~~~~~~~~~~~

    :copyright: (c) 2016 by Andrew Bednar.
"""
import os

# Might reconsider root path attribute in the app creation
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False


class DevelopmenConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False

config_by_name = dict(dev=DevelopmenConfig,
                      test=TestingConfig,
                      prod=ProductionConfig)