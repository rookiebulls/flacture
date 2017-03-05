# -*- coding: utf-8 -*-
"""
    flacture.api.token
    ~~~~~~~~~~~~~~~~~~

    generate api token
"""

from flask import Blueprint, request
from flask_json import JsonError, as_json

from ..errors import Unauthorized
from ..models import UserService


bp = Blueprint('token', __name__, url_prefix='/api/v1/auth')


@bp.route('/token', methods=['POST'])
@as_json
def generate_token():
    """Generate a token"""
    auth = request.get_json(force=True)
    name = auth.get('name')
    password = auth.get('password')
    user = UserService().first(name=name)
    if user is None:
        raise JsonError(error_msg='no such user')
    if not user.verify_password(password):
        raise Unauthorized(error_msg='wrong password')
    token = user.generate_auth_token()
    return {'name': name, 'token': token}
