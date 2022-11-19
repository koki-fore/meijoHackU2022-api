from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from .base import TimestampMixin
from db import Base


class Challenge(Base, TimestampMixin):
    __tablename__ = "challenges"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    text = Column(String(255))
    experience_point = Column(Integer, default=0, nullable=False)
    
    posts = relationship("Post", back_populates="challenge")