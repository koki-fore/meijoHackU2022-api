from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True)
    user_FK = Column(Integer, ForeignKey('users.id'))
    challenge_FK = relationship('Challenge')
    text = Column(String(255))
    picture_path_01 = Column(String(255))
    picture_path_02 = Column(String(255))
    picture_path_03 = Column(String(255))
    picture_path_04 = Column(String(255))
    like_count = Column(Integer)