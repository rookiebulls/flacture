# -*- coding: utf-8 -*-
"""
flacture.models
~~~~~~~~~~~~~~~

flacture models package
"""

from .user_model import User
from ..helpers import Service
from ..errors import ValidationError


class UserService(Service):
    __model__ = User

    def _preprocess_params(self, kwargs):
        super(UserService, self)._preprocess_params(kwargs)
        try:
            name = kwargs['name']
            email = kwargs['email']
            password = kwargs['password']
        except KeyError:
            raise ValidationError(error_msg='name, email and password \
                                  are required!')
        return dict(name=name, email=email, password=password)
