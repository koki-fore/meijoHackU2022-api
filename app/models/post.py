from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True)
    user_FK = Column(Integer, ForeignKey('users.id'))
    challenge_FK = Column(Integer, ForeignKey('challenges.id'), nullable=True)
    text = Column(String(255), nullable=False)
    picture_path_01 = Column(String(255))
    picture_path_02 = Column(String(255))
    picture_path_03 = Column(String(255))
    picture_path_04 = Column(String(255))
    like_count = Column(Integer, default=0, nullable=False)
    
    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    challenge = relationship("Challenge", back_populates="posts")