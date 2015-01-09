from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import json

from sqlalchemy import types

__all__ = ['JSON']


class JSON(types.TypeDecorator):
    """
    Store JSON-serialized objects. Note that these objects are not "mutable" in
    that the sqlalchemy session will not detect and persist changes to a
    persisted object (e.g. for dicts or lists). To store changes to these
    objects, create a whole new object by way of .copy().
    """
    impl = types.Text

    def process_bind_param(self, value, dialect):
        # Convert from object to serialized JSON for DB storage.
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        # Convert from serialized JSON from DB to object.
        return json.loads(value)
