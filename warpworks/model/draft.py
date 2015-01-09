from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from sqlalchemy import Column, types

from . import custom_types
from .base import Base
from .image import ImageMixin
from .user_mixin import UserMixin

__all__ = ['DraftMeta']


class DraftMeta(Base, ImageMixin, UserMixin):
    __tablename__ = 'drafts'
    __table_args__ = {'mysql_engine': 'InnoDB'}
    id = Column(types.Integer, primary_key=True)
    title = Column(types.Unicode(255), nullable=False)
    draft_json = Column(custom_types.JSON, nullable=False)
