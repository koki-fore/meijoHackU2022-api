from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from .base import TimestampMixin
from app.db import Base


class Like(Base, TimestampMixin):
    __tablename__ = "likes"
    
    id = Column(Integer, primary_key=True)
    user_FK = Column(Integer, ForeignKey('users.id'))
    post_FK = Column(Integer, ForeignKey('posts.id'))