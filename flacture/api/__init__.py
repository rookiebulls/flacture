# -*- coding: utf-8 -*-
"""
    flacture.api
    ~~~~~~~~~~~~

    flacture api package
"""

from functools import wraps

from flask_json import as_json

from .. import create_app as factory_create
from ..auth import auth


def create_app(config_override=None):
    app = factory_create('flacture', __path__, config_override=config_override)

    return app


def route(bp, *args, **kwargs):
    kwargs.setdefault('strict_slashes', False)

    def decorator(f):
        @bp.route(*args, **kwargs)
        @as_json
        @auth.login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            rv = f(*args, **kwargs)
            return rv
        return wrapper
    return decorator
