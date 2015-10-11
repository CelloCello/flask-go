# -*- coding: utf-8 -*-
import os

from flask import Flask

import settings


def _config_app(app):
    """set flask config
    """
    app.config.from_object(settings.SYSTEM_CONFIG_PATH)


def _config_ext(app):
    """set config of extensions
    """
    pass


def _set_blueprints(app):
    for bp, prefix in settings.SYSTEM_BLUEPRINTS:
        print "blueprint: %s, prefix: %s" % (bp.name, prefix)
        print "root_path: " + bp.root_path
        app.register_blueprint(bp, url_prefix=prefix)


def create_app(app_name):
    """create Flask app
    """
    app = Flask(app_name)
    _config_app(app)
    _config_ext(app)
    _set_blueprints(app)

    return app
