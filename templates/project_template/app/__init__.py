# -*- coding: utf-8 -*-

from flask import Flask
from .config import (
    ProductionConfig,
    DevelopmentConfig,
    TestingConfig
)

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

from app import routes
