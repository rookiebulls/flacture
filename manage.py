# -*- coding: utf-8 -*-
"""
    manage
    ~~~~~~~~~~~~

    manager module
"""

from flask_script import Manager

from flacture import db
from flacture.api import create_app
from flacture.models import UserService

app = create_app()
manager = Manager(app)


@manager.command
def initdb(drop_first=False):
    if drop_first:
        db.drop_all()
    db.create_all()
    UserService().create(name='admin', password='admin', email='admin@gmail.com')


if __name__ == '__main__':
    manager.run()
