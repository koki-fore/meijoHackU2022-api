import sys

sys.path.append('/app')

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from .base import TimestampMixin
from db import Base


class Challenge_category(Base, TimestampMixin):
    __tablename__ = "challenge_categories"
    
    id = Column(Integer, primary_key=True)
    challenge_FK = Column(Integer, ForeignKey('challenges.id'))
    category_FK = Column(Integer, ForeignKey('categories.id'))