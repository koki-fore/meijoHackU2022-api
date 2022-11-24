import sys

sys.path.append('/app')

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from .base import TimestampMixin
from db import Base


class Challenge_completed(Base, TimestampMixin):
    __tablename__ = "challenge_completed"
    
    id = Column(Integer, primary_key=True)
    challenge_FK = Column(Integer, ForeignKey('challenges.id'))
    user_FK = Column(Integer, ForeignKey('users.id'))
    
    user = relationship("User", back_populates="challenge_completed")