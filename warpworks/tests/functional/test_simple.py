from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from unittest import TestCase

import transaction

from webtest import TestApp

from ...main import main
from ... import model

from ..settings import settings


app = main({}, **settings)


def setup():
    model.Base.metadata.drop_all()
    model.Base.metadata.create_all()

    with transaction.manager:
        root_user = model.User(
            name=u'Bot',
            email='root@warpworks.local',
        )
        root_user.update_password('root')
        model.Session.add(root_user)


class FunctionalBase(TestCase):

    def setUp(self):
        self.app = TestApp(app)


class TestSmoke(FunctionalBase):

    def test_index(self):
        self.app.get('/')
