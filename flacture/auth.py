# -*- coding: utf-8 -*-
"""
    flacture.auth
    ~~~~~~~~~~~~~

    authorization module
"""

from flask import g
from flask_httpauth import HTTPTokenAuth

from .errors import Unauthorized
from .models.user_model import User


auth = HTTPTokenAuth('Bearer')


@auth.error_handler
def auth_error():
    raise Unauthorized(error_msg='Unauthorized Access!!!!')


@auth.verify_token
def verify_token(token):
    g.user = User.verify_auth_token(token)
    return g.user is not None
