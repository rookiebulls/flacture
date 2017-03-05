# -*- coding: utf-8 -*-
"""
flacture.errors
~~~~~~~~~~~~~~~

errors and handler
"""

from flask_json import json_response


class FlactureException(Exception):
    def __init__(self, error_msg):
        self.error_msg = error_msg


class Unauthorized(FlactureException):
    pass


class ValidationError(FlactureException):
    pass


def on_not_found(e):
    return json_response(status_=404, error_msg=str(e))


def on_not_allowed(e):
    return json_response(status_=405, error_msg=str(e))


def on_unauthorized(e):
    return json_response(status_=401, error_msg=e.error_msg)


def on_not_validated(e):
    return json_response(status_=400, error_msg=e.error_msg)
