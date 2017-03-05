# -*- coding: utf-8 -*-
"""
    flacture.api.users
    ~~~~~~~~~~~~~~~~~~

    users endpoint
"""

from flask import Blueprint, request

from . import route
from ..models import UserService
from ..errors import ValidationError


bp = Blueprint('users', __name__, url_prefix='/api/v1/users')


@route(bp, '/', methods=['GET'])
def users():
    """Get all users"""
    users = UserService().all()
    return dict(data=users)


@route(bp, '/<int:id>', methods=['GET'])
def get_user(id):
    """Get a user"""
    user = UserService().get_or_404(id)
    return dict(data=user)


@route(bp, '/', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.get_json(force=True)
    user_by_name = UserService().first(name=data['name'])
    user_by_email = UserService().first(email=data['email'])
    if user_by_name is not None:
        raise ValidationError(error_msg='user has been registered!')
    if user_by_email is not None:
        raise ValidationError(error_msg='email has been registered!')
    user = UserService().create(**data)
    return dict(data=user)


@route(bp, '/<int:id>', methods=['PUT'])
def update_user(id):
    """Update a user"""
    user = UserService().get_or_404(id)
    data = request.get_json(force=True)
    updated_user = UserService().update(user, **data)
    return dict(data=updated_user)


@route(bp, '/<int:id>', methods=['DELETE'])
def delete_user(id):
    """Delete a user"""
    user = UserService().get_or_404(id)
    UserService().delete(user)
    return dict(data=True)
