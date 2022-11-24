import sys

sys.path.append('/app')

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from .base import TimestampMixin
from db import Base


class Follow(Base, TimestampMixin):
    __tablename__ = "follows"
    
    id = Column(Integer, primary_key=True)
    follower_id = Column(Integer, ForeignKey('users.id'))
    followee_id = Column(Integer, ForeignKey('users.id'))