from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from .base import TimestampMixin
from app.db import Base


class User(Base, TimestampMixin):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    firebase_FK = Column(String(1024), nullable=False, unique=True)
    user_id = Column(String(1024), nullable=False, unique=True)
    screen_name = Column(String(1024), nullable=False)
    first_name = Column(String(1024))
    last_name = Column(String(1024))
    experience_point_num = Column(Integer, default=0)
    profile_picture_path = Column(String(1024), nullable=True)
    description = Column(String(1024))
    follower_num = Column(Integer, default=0)
    followee_num = Column(Integer, default=0)