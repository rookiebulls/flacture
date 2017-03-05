# -*- coding: utf-8 -*-
"""
    flacture.models.user_model
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    user model
"""

from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from werkzeug.security import generate_password_hash, check_password_hash

from .. import db
from ..helpers import JsonSerializer


class UserJsonSerializer(JsonSerializer):
    # __json_public__ = ['name', 'email']
    __json_hidden__ = ['password_hash']
    __json_modifiers__ = {'name': lambda name, self: name + '_fixed'}


class User(UserJsonSerializer, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(255), unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def generate_auth_token(self, expires_in=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expires_in)
        return s.dumps({'id': self.id}).decode('utf-8')

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return None
        return User.query.get(data['id'])
