import sys

sys.path.append('/app')

from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from .base import TimestampMixin
from db import Base


class User(Base, TimestampMixin):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    firebase_FK = Column(String(20), nullable=False, unique=True)
    user_id = Column(String(20), nullable=False, unique=True)
    screen_name = Column(String(20), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    experience_point_num = Column(Integer, default=0, nullable=False)
    profile_picture_path = Column(String(20))
    description = Column(String(255))
    follower_num = Column(Integer, default=0, nullable=False)
    followee_num = Column(Integer, default=0, nullable=False)
    
    posts = relationship("Post", back_populates="user")
    comments = relationship("Comment", back_populates="user")
    likes = relationship("Like", back_populates="user")
    challenge_completed = relationship("Challenge_completed", back_populates="user")