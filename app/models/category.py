from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text
from sqlalchemy.orm import relationship

from .base import TimestampMixin
from app.db import Base

class Category(Base, TimestampMixin):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    